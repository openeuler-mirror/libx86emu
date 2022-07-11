%global make_flags \\\
        LIBDIR=%{_libdir} \\\
        GIT2LOG=: \\\
        VERSION=%%{version} \\\
        MAJOR_VERSION=%%(echo %{version} |cut -d. -f1) \\\
        CFLAGS="-fPIC %{optflags}" \\\
        LDFLAGS="-fPIC %{__global_ldflags}"

Name:           libx86emu
Version:        3.1
Release:        3
Summary:        x86 emulation library
License:        BSD
URL:            https://github.com/wfeldt/libx86emu
Source0:        https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc

%description
libx86emu is a small library to emulate x86 instructions. 
The focus here is not a complete emulation (go for qemu for this) 
but to cover enough for typical firmware blobs.

%package        devel
Summary:        Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build %{make_flags} shared

%ldconfig_scriptlets

%install
%make_install %{make_flags}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_libdir}/libx86emu.so.*

%files          devel
%defattr(-,root,root)
%{_includedir}/x86emu.h
%{_libdir}/libx86emu.so

%changelog
* Mon Jul 11 2022 wangkerong <wangkerong@h-partners.com> - 3.1-3
- add missig requires

* Fri Nov 5 2021 xingxing <xingxing9@huawei.com> - 3.1-2
- ID:NA
- SUG:NA
- DESC:delete low version  

* Tue Jul 28 2020 zhangqiumiao <zhangqiumiao1@huawei.com> - 3.1-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:upgrade to version 3.1

* Mon Sep 2 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11-4
- Package init
