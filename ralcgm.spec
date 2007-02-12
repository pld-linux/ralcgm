Summary:	CGM metafiles interpreter and translator
Summary(pl.UTF-8):   Interpreter i konwerter plików CGM
Name:		ralcgm
Version:	3.50
Release:	3
Group:		Applications/Graphics
License:	non-profit - see README
Source0:	ftp://ftp.cc.rl.ac.uk/pub/graphics/ralcgm/unix/%{name}-%{version}.tar.Z
# Source0-md5:	c132d8533527c35eb99581ed7cc738db
Patch0:		%{name}-linux.patch
URL:		http://www.agocg.ac.uk/train/cgm/ralcgm.htm
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RAL-CGM is a program to translate or interpret CGM (Computer Graphics
Metafile) files, either to a different encoding (Binary, Character or
Clear Text) or to view on a terminal or to send to a plotter
(PostScript or HPGL).

It can be used as ImageMagick delegate to convert from CGM format.

%description -l pl.UTF-8
RAL-CGM jest programem do interpretowania i konwersji plików CGM
(Computer Graphics Metafile) do innych formatów lub w celu
wyświetlenia albo wydrukowania.

Może być używany przez ImageMagick do konwersji z formatu CGM.

%prep
%setup -q -c
%patch0 -p1

%build
OPT="%{rpmcflags}" \
./CGMconfig linux <<EOF

y



y
y
y
y
n
/usr/X11R6/%{_lib}
y
n
y
y
y
EOF

%{__make} -C src cgmfile.o cgmerr.o genbez genher

sed -e "s@^\\(#define DATADIR\\).*@\\1 \"%{_datadir}/ralcgm/\"@" \
	include/mach.h > mach.h.tmp
mv -f mach.h.tmp include/mach.h

rm -f src/cgm{file,err}.o
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/ralcgm,%{_mandir}/man1}

install bin/ralcgm $RPM_BUILD_ROOT%{_bindir}
install data/* $RPM_BUILD_ROOT%{_datadir}/ralcgm
install docs/ralcgm.man $RPM_BUILD_ROOT%{_mandir}/man1/ralcgm.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ralcgm
%{_mandir}/man1/*
