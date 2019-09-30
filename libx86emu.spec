%global make_flags \\\
        LIBDIR=%{_libdir} \\\
        GIT2LOG=: \\\
        VERSION=%%{version} \\\
        MAJOR_VERSION=%%(echo %{version} |cut -d. -f1) \\\
        CFLAGS="-fPIC %{optflags}" \\\
        LDFLAGS="-fPIC %{__global_ldflags}"

Name:           libx86emu
Version:        1.11
Release:        4
Summary:        x86 emulation library
License:        BSD
URL:            https://github.com/wfeldt/libx86emu
Source0:        https://github.com/wfeldt/libx86emu/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         libx86emu-1.11-ldflags.patch
BuildRequires:  gcc

%description
libx86emu is a small library to emulate x86 instructions. 
The focus here is not a complete emulation (go for qemu for this) 
but to cover enough for typical firmware blobs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

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
%{_libdir}/*.so.*

%files          devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Mon Sep 2 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11-4
- Package init
