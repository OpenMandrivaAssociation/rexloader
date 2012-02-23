%define 	svn 207

Name:		rexloader
Version:	0.1a.rev%{svn}
Release:	%mkrel 1
Summary:	Advanced download manager with Qt4 GUI
Group:		Networking/File transfer
License:	GPLv3
URL:		http://code.google.com/p/rexloader/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		rexloader-0.1a-linkage.patch
BuildRequires:	qt4-devel
BuildRequires:	zlib-devel

%description
Advanced Qt4 download manager over HTTP with configurable
multithreaded downloading.

%prep
%setup -q
%patch0 -p1

%build
cd Httploader
%qmake_qt4 HttpLoader.pro
%__make
cd ../NoticeWindow
%qmake_qt4 NoticeWindow.pro
%__make
cd ../REXLoader
%qmake_qt4 REXLoader.pro
%__make

%install
%__rm -rf %{clean}
%__mkdir_p %{buildroot}%{_bindir}
%__install ./usr/bin/REXLoader %{buildroot}%{_bindir}/%{name}
%__mkdir_p %{buildroot}%{_libdir}/%{name}/plugins
%__install ./usr/lib/%{name}/plugins/* %{buildroot}%{_libdir}/%{name}/plugins
%__install ./NoticeWindow/NoticeWindow %{buildroot}%{_libdir}/%{name}/plugins/libNoticeWindow.so
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install ./REXLoader/images/RExLoader_64x64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=REXLoader
Comment=Download manager
Comment[ru]=Менеджер закачек
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Network;FileTransfer;
EOF

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}

