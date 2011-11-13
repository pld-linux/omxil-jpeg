Summary:	JPEG image decoder component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent dekodujący obrazy JPEG dla implementacji Bellagio OpenMAX IL
Name:		omxil-jpeg
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxjpeg-%{version}.tar.gz
# Source0-md5:	4985931601103c65b915c9ed0b82a695
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
JPEG component is an image decoder component for Bellagio OpenMAX IL
that uses IJG libjpeg library for JPEG image decoding.

%description -l pl.UTF-8
Komponent JPEG to komponent dekodujący obrazy dla implementacji
Bellagio OpenMAX IL, wykorzystujący bibliotekę IJG libjpeg do
dekodowania obrazów JPEG.

%prep
%setup -q -n libomxjpeg-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomximagejpeg.so*
