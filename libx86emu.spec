%global make_flags \\\
        LIBDIR=%{_libdir} \\\
        GIT2LOG=: \\\
        VERSION=%%{version} \\\
        MAJOR_VERSION=%%(echo %{version} |cut -d. -f1) \\\
        CFLAGS="-fPIC %{optflags}" \\\
        LDFLAGS="-fPIC %{__global_ldflags}"

Name:           libx86emu
Version:        3.5
Release:        1
Summary:        x86 emulation library
License:        BSD
URL:            https://github.com/wfeldt/libx86emu
Source0:        https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc

%description
Small x86 emulation library with focus of easy usage and extended execution
logging functions. The library features an API to create emulation objects
for x86 architecture.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%make_build %{make_flags} shared

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
* Fri Mar 25 2022 liukuo <liukuo@kylinos.cn> - 3.5-1
- Update version to v3.5

* Fri Nov 5 2020 xingxing <xingxing9@huawei.com> - 3.1-2
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
