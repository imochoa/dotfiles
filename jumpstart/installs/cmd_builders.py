#!/usr/bin/env python3

# std imports
from typing import Union, Sequence, Dict, Tuple, Optional


# local imports


def aptget_install(pkgs: Union[str, Sequence[str]],
                   ppas: Union[None, str, Sequence[str]] = None,
                   shebang: str = "#!/usr/bin/env bash\n",
                   ) -> str:
    """

    """
    cmd_str = shebang

    if ppas is not None:
        if isinstance(ppas, str):
            ppas = [ppas]
        for ppa in ppas:
            cmd_str += f"sudo add-apt-repository {ppa} && "
        cmd_str += "sudo apt-get update -y"

    if isinstance(pkgs, str):
        pkgs = [pkgs]
    return f"{cmd_str}\nsudo apt-get install -y {' '.join(pkgs)}"


def aptget_remove(pkgs: Union[str, Sequence[str]],
                  ppas: Union[None, str, Sequence[str]] = None,
                  shebang: str = "#!/usr/bin/env bash\n",
                  ) -> str:
    """

    """
    cmd_str = shebang

    if ppas is not None:
        if isinstance(ppas, str):
            ppas = [ppas]
        for ppa in ppas:
            cmd_str += f"sudo add-apt-repository --remove {ppa} && "
        cmd_str += "sudo apt-get update -y"

    if isinstance(pkgs, str):
        pkgs = [pkgs]
    return f"{cmd_str}\nsudo apt remove -y {' '.join(pkgs)}"


def snap_install(pkgs: Union[str, Sequence[str]],
                 channels: Union[None, str, Sequence[str]] = None,
                 shebang: str = "#!/usr/bin/env bash\n",
                 ) -> str:
    """

    """
    cmd_str = shebang

    if isinstance(pkgs, str):
        pkgs = [pkgs]

    if isinstance(channels, str):
        channels = [channels.strip()]

    channels = [c.strip() for c in channels if isinstance(c, str)]
    channels = [c for c in channels if c]

    if not channels:
        channels = ['--classic' for _ in pkgs]

    if len(pkgs) > len(channels):
        channels += (len(pkgs) - len(channels)) * [channels[-1]]

    for idx, c in enumerate(channels):
        if c.startswith('--'):
            continue
        elif c.startswith('-'):
            channels[idx] = f'-{c}'
        else:
            channels[idx] = f'--{c}'

    for p, c in zip(pkgs, channels):
        cmd_str += f"sudo snap install {c} {p}\n"

    return cmd_str


def snap_remove(pkgs: Union[str, Sequence[str]],
                channels: Union[None, str, Sequence[str]] = None,
                shebang: str = "#!/usr/bin/env bash\n",
                ) -> str:
    """

    """
    cmd_str = shebang

    if isinstance(pkgs, str):
        pkgs = [pkgs]

    for p in pkgs:
        cmd_str += f"sudo snap remove {p}\n"

    return cmd_str
