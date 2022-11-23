### Scan Uninstaller Settings in Your Registry

Is a little script I wrote when I try to uninstall an old MSVC runtime package but cannot find its uninstall package.

This script will scan the registry of uninstall list (`SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall` and `SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall`) and find the item that match the name you search. And it also scan the corresponding item in `HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products`, which register the software to the system.

In my case, I failed to install 3dsmax 2012 because it rely on the package `Microsoft Visual C++ 2005 Redistributable`, which  has been an older version in my system. So the installer try to uninstall it before install the new one, and failed because the uninstaller is broken. Then I try to download the installer of this version on microsoft website, but still didn't work for me. Finally I wrote this scanner and just delete the item in registry, which seems not so elegant (because there maybe something else of the package left in my system), but it just work.

#### Usage

```
python3 main.py
```

And just type a regex of what you wanna search. And it will print out some information

q for quit

```
X:\xxx\uninstaller_scan>python main.py
> 2005
=== Microsoft Visual C++ 2005 Redistributable ===
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{837b34e3-7c30-493c-8f6a-2b0f04e2912c}
        AuthorizedCDFPrefix:
        Comments:
        Contact:
        DisplayVersion: 8.0.59193
        HelpLink:
        HelpTelephone:
        InstallDate: 20221123
        InstallLocation:
        InstallSource: C:\Users\root\AppData\Local\Temp\IXP001.TMP\
        ModifyPath: MsiExec.exe /X{837b34e3-7c30-493c-8f6a-2b0f04e2912c}
        NoModify: 1
        NoRepair: 1
        Publisher: Microsoft Corporation
        Readme:
        Size:
        EstimatedSize: 2768
        UninstallString: MsiExec.exe /X{837b34e3-7c30-493c-8f6a-2b0f04e2912c}
        URLInfoAbout:
        URLUpdateInfo:
        VersionMajor: 8
        VersionMinor: 0
        WindowsInstaller: 1
        Version: 134276921
        Language: 0
        ShimFlags: 512
        DisplayName: Microsoft Visual C++ 2005 Redistributable
= Product = : HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products\3e43b73803c7c394f8a6b2f0402e19c2


=== Microsoft Visual Studio 2005 Remote Debugger Light (x64) - ENU ===
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{542DDF04-9F91-4F36-B2F4-2638B788A4C8}
        AuthorizedCDFPrefix:
        Comments:
        Contact:
        DisplayVersion: 8.0.52572
        HelpLink:
        HelpTelephone:
        InstallDate: 20170710
        InstallLocation:
        InstallSource: K:\PreReqs\RemoteDebugger\
        NoModify: 1
        NoRemove: 1
        NoRepair: 1
        Publisher: Microsoft Corporation
        Readme:
        Size:
        EstimatedSize: 17583
        SystemComponent: 1
        URLInfoAbout:
        URLUpdateInfo:
        VersionMajor: 8
        VersionMinor: 0
        WindowsInstaller: 1
        Version: 134270300
        Language: 1033
        DisplayName: Microsoft Visual Studio 2005 Remote Debugger Light (x64) - ENU
        sEstimatedSize2: 10883
= Product = : HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products\40FDD24519F963F42B4F62837B884A8C


=== Microsoft Visual C++ 2005 Redistributable (x64) ===
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\{ad8a2fa1-06e7-4b0d-927d-6e54b3d31028}
        AuthorizedCDFPrefix:
        Comments:
        Contact:
        DisplayVersion: 8.0.61000
        HelpLink:
        HelpTelephone:
        InstallDate: 20170902
        InstallLocation:
        InstallSource: C:\Users\root\AppData\Local\Temp\IXP000.TMP\
        ModifyPath: MsiExec.exe /X{ad8a2fa1-06e7-4b0d-927d-6e54b3d31028}
        NoModify: 1
        NoRepair: 1
        Publisher: Microsoft Corporation
        Readme:
        Size:
        EstimatedSize: 11165
        UninstallString: MsiExec.exe /X{ad8a2fa1-06e7-4b0d-927d-6e54b3d31028}
        URLInfoAbout:
        URLUpdateInfo:
        VersionMajor: 8
        VersionMinor: 0
        WindowsInstaller: 1
        Version: 134278728
        Language: 0
        DisplayName: Microsoft Visual C++ 2005 Redistributable (x64)
        sEstimatedSize2: 7000
= Product = : HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products\1af2a8da7e60d0b429d7e6453b3d0182


```

The first line display the package name, which match the name display in *Uninstall or remove apps and programs*

The second line indicate the key in registry of uninstall list

The last line indicate the key in registry of product




