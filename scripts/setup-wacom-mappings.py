#!/usr/bin/python3
import os
import subprocess
import re
import pdb
import sys
from enum import Enum, auto

class PadButtons(Enum):
    FAR_LEFT_P = auto()
    MID_LEFT_P = auto()
    MID_RIGHT_P = auto()
    FAR_RIGHT_P = auto()

class StylusButtons(Enum):
    TIP_S = auto()
    LOWER_S = auto()
    UPPPER_S = auto()


WACOM_BUTTON_MAP = {
    # DEVICES
    "Wacom Intuos BT S".lower(): {
        # PAD
            PadButtons.FAR_LEFT_P:1,
            PadButtons.MID_LEFT_P:2,
            PadButtons.MID_RIGHT_P:3,
            PadButtons.FAR_RIGHT_P:8,
        # STYLUS
            StylusButtons.TIP_S:1,
            StylusButtons.LOWER_S:2,
        }
}

WACOM_KEYMAP={
        # PAD
            PadButtons.FAR_LEFT_P:"key ctrl z",
            PadButtons.MID_LEFT_P:"key ctrl y",
            PadButtons.MID_RIGHT_P:"key pgup",
            PadButtons.FAR_RIGHT_P:"key pgdn",
        # STYLUS
            StylusButtons.TIP_S:None, # You probably don't want to remap this
            StylusButtons.LOWER_S:None,
}

if __name__=='__main__':

    p = subprocess.check_output(['xsetwacom', '--list', 'devices'])

    if not p:
        sys.stdout.write('\n\nNo wacom devices found!\n\n')
        sys.exit(1)

    p=p.decode('ascii')
    matched_devices=dict()

    for l in p.split('\n'):
        l = l.strip().lower()

        try:
            device_k=next(k for k in WACOM_BUTTON_MAP if l.startswith(k))
            matched_devices.setdefault(device_k,dict())

            # Index of match
            result = re.findall(r'\d+',l)
            idx = int(result[-1])

            # stylus or pad
            if l.endswith('PAD'.lower()):
                matched_devices[device_k].update({PadButtons : idx})
            elif l.endswith('STYLUS'.lower()):
                matched_devices[device_k].update({StylusButtons : idx})
        except StopIteration:
            pass

    sys.stdout.write("Found:\n {}\n\n".format(matched_devices.keys()))

    sys.stdout.write("Mapping the keys...\n\n")
    for device_name, device_idx_map in matched_devices.items():

        if device_name not in WACOM_BUTTON_MAP:
            sys.stdout.write("No mapping for device: {}\n".format(device_name))
            continue
        button_idx_map = WACOM_BUTTON_MAP[device_name]

        for button, key in WACOM_KEYMAP.items():

            if not key:
                sys.stdout.write("\tNo mapping for {} -> skipping!\n".format(button))
                continue
            sys.stdout.write("\tSetting {} -> {}\n".format(button,key))
            bp = subprocess.check_output(
                 ['xsetwacom',
                  '--set',
                  str(device_idx_map[type(button)]),
                  'button',
                  str(button_idx_map[button]),
                  key])

    sys.stdout.write('\nDone setting the mappings!\n\n')

# Parameters
# Not all parameters are available on all tools.  Use the get command with the parameter or "all" parameter for specific input tool applicable parameters and current settings.
# 
# Area x1 y1 x2 y2
# Set the tablet input area in device coordinates in the form top left x/y and bottom right x/y. Top left and bottom right are defined in the device's native orientation, regardless of the actual rotation currently applied. Input outside of these coordinates will be clipped to the edges of the area defined.  Default:  0 0 x2 y2; with x2 and y2 tablet specific.
# 
# Button button-number [mapping]
# Set a mapping for the specified button-number. Mappings take the form of either a single numeric button or an 'action' to be performed. If no mapping is provided, the default mapping is restored. If button-number is mapped to 0, the Button event is ignored.
# 
# Numeric button mappings indicate what X11 button number the given button-number should correspond to. For example, a mapping of "3" means a press of the given button-number will produce a press of X11 button 3 (i.e. right click).
# 
# Action mappings allow button presses to perform many events. They take the form of a string of keywords and arguments.
# 
# The "key" keyword is followed by a list of key names. These can optionally be preceded by "+" for press and "-" for release. If +/- is not given, press-and-release is assumed, except for modifier keys which are left pressed. Key names can be X11 KeySyms or some aliases such as 'shift' or 'f1' (the full list can be seen with the list modifiers command).
# 
# To assign a key that is not in the modifiers list, use the KeySym in /usr/include/X11/keysymdef.h with the XK_ prefix removed or its actual value as is. For example, XK_BackSpace should be specified as "BackSpace". "0xff80" can also be used to replace "BackSpace" since it's the unique KeySym value of Backspace key.
# 
# Here is a combined example: "key +a shift b shift -a 0xff0d" converts the button into a series of keystrokes. In this example, "press a, press shift, press and release b, release shift, release a, then press and release enter". "key +a +shift b -shift -a 0xff0d" does the same thing.
# 
# The "button" keyword is similar except that its arguments are X11 button numbers.
# 
# The "modetoggle" keyword is also recognized; it takes no arguments, and toggles the device mode between relative and absolute pointer tracking.
# 
# The "pan" keyword causes the driver to send scroll events while the pen is dragged. This makes it easy to scroll through lists and documents, pan around 2D canvases, and zoom in/out of 3D scenes (exact behavior depends on application interpretation of scrollwheel events). Dragging the pen up/down will send scrollwheel down/up events; dragging it left/right will send scrollwheel right/left events.
# 
# The events in the action mapping are sent when the physical button is pressed. If the action mapping leaves any buttons or keys pressed (such as a modifier key), they will be released when the physical button is released.
# 
# Multiple keywords may be present in one action if desired: for example "key +ctrl button 5 key -ctrl". Each keyword takes all arguments until the next keyword.
# 
# A maximum of 256 presses and/or releases can be specified in an action mapping.
# 
# The driver can only simulate physical key events but not keysyms and xsetwacom translates the mapping sequence into such events. Thus, symbols on the same physical key will generate the same event. For example, '1' and '!' are on the same key on a US keyboard and thus have the same keycode).  For access to keys on a higher shift level, the sequence should be entered as it would be typed on a physical keyboard. For example, a exclamation mark is entered by the sequence of "key +shift 1 -shift".
# 
# BindToSerial [serial|0]
# Bind the device to the tool with the specified serial number. Once bound, the device will ignore events from other tools. A serial of 0 means the device is unbound and will react to any tool of the matching type. Default: 0
# 
# MapToOutput [output]
# Map the tablet's input area to a given output (e.g. "VGA1"). Output names may either be the name of a head available through the XRandR extension, or an X11 geometry string of the form WIDTHxHEIGHT+X+Y. To switch to the next available output, the "next" keyword is also supported. This will cycle between the individual monitors connected to the system, and then the entire desktop. The mapping may be reset to the entire desktop at any time with the output name "desktop". Users of the NVIDIA binary driver should use the output names "HEAD-0" and "HEAD-1" until the driver supports XRandR 1.2 or later.
# 
# The output mapping configuration is a onetime setting and does not track output reconfigurations; the command needs to be re-run whenever the output configuration changes. When used with tablet rotation, the tablet must be rotated before it is mapped to the new screen. This parameter is write-only and cannot be queried.
# 
# Mode Absolute|Relative
# Set the device mode as either Relative or Absolute. Relative means pointer tracking for the device will function like a mouse, whereas Absolute means the pointer corresponds to the device's actual position on the tablet or tablet PC screen.  Default:  Absolute for stylus, eraser and tablet PC touch; Relative for cursor and tablet touch.
# 
# PressureCurve x1 y1 x2 y2
# A Bezier curve of third order, composed of two anchor points (0,0 and 100,100) and two user modifiable control points that define the curve's shape.  Raise the curve (x1<y1 x2<y2) to "soften" the feel and lower the curve (x1>y1 x2>y2) for a "firmer" feel.  Sigmoid shaped curves are permitted (x1>y1 x2<y2 or x1<y1 x2>y2).  Default:  0 0 100 100, a linear curve; range of 0 to 100 for all four values.
# 
# RawSample level
# Set the sample window size (a sliding average sampling window) for incoming input tool raw data points.  Default:  4, range of 1 to 20.
# 
# Rotate none|half|cw|ccw
# Set the tablet to the given rotation:
#  none: the tablet is not rotated and uses its natural rotation
#  half: the tablet is rotated by 180 degrees (upside-down)
#  cw: the tablet is rotated 90 degrees clockwise
#  ccw: the tablet is rotated 90 degrees counter-clockwise
# 
# Rotation is a tablet-wide option: rotation of one tool affects all other tools associated with the same tablet. When the tablet is physically rotated, rotate any tool to the corresponding orientation.  Default:  none
# 
# Suppress level
# Set the delta (difference) cutoff level for further processing of incoming input tool coordinate values.  For example a X or Y coordinate event will be sent only if the change between the current X or Y coordinate and the previous one is greater than the Suppress value.  The same applies to pressure level (Z coordinate) and Tilt rotation values.  With a current absolute wheel (AbsWheel) or Tilt value the delta between it and the previous value must be equal to or greater than the Suppress value in order to be sent on.  Suppress is a tablet wide parameter.  A specified delta level for one input tool is applied to all input tool coordinates.  To disable suppression use a level of 0.  Default:  2, range of 0 to 100.
# 
# TabletDebugLevel level
# Set the debug level for this tablet to the given level. This only affects code paths that are shared between several tools on the same physical tablet. A higher level means more fine-grained debug messages, a level of 0 turns debugging off for this tool. Requires the driver to be built with debugging enabled. See also ToolDebugLevel.  Default:  0, range of 0 to 12.
# 
# TabletPCButton on|off
# If on, the stylus must be in contact with the screen for a stylus side button to work.  If off, stylus buttons will work once the stylus is in proximity of the tablet (regardless of whether it is touching the screen).  Default:  on for Tablet PCs; off for all other models.
# 
# ToolSerialPrevious
# Get the serial number of the tool that was last in proximity last. This serial number is updated whenever the tool goes out of proximity. If the current tool went out of proximity once, this serial number is the one of the current tool. This is a read-only parameter.
# 
# Touch on|off
# If on, touch events are reported to userland, i.e., system cursor moves when user touches the tablet. If off, touch events are ignored. Default: on for devices that support touch; off for all other models.
# 
# HWTouchSwitchState on|off
# If on, it means touch switch is turned off. That is, touch events are reported to userland. If off, touch switch is turned on, i.e., touch events are ignored. This is a read-only parameter. Initial touch switch state is retrieved from the kernel when X driver starts.
# 
# CursorProximity distance
# Set the distance at which a relative tool is treated as being out of proximity. Beyond this distance the cursor will stop responding to tool motion. The default value for pucks is 10 (Intuos Pro) or 42 (Intuos/Bamboo). The default value for pens is 30.
# 
# Threshold level
# Set the minimum pressure necessary to generate a Button event for the stylus tip, eraser, or touch.  The pressure levels of all tablets are normalized to 2048 levels irregardless of the actual hardware supported levels.  This parameter is independent of the PressureCurve parameter.  Default:  27, range of 0 to 2047.
# 
# ToolDebugLevel level
# Set the debug level for this tool to the given level. This only affects code paths that are specific to a given tool. A higher level means more fine-grained debug messages, a level of 0 turns debugging off for this tool. Requires the driver to be built with debugging enabled. See also TabletDebugLevel.  Default:  0, range of 0 to 12.
# 
# PressureRecalibration on|off
# If the initial pressure of a device is != 0 the driver recalibrates the pressure range. This is to account for worn out devices. The downside is that when the user hits the tablet very hard the initial pressure reading may be unequal to zero even for a perfectly good pen. If the consecutive pressure readings are not higher than the initial pressure by a threshold no button event will be generated. This option allows to disable the recalibration.  Default:  on
# 
# PanScrollThreshold distance
# This specifies the distance the pen must move (in tablet units) before a scroll event is generated when using the "pan" action. Smaller values will require less distance and be more sensitive. Larger values will require more distance and be less sensitive.  Default: 1300 or 2600 depending on tablet resolution (corresponds to 13 mm of distance).
