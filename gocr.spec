Summary:	OCR (Optical Character Recognition) program
Name:		gocr
Version:	0.50
Release:	9
License:	GPLv2
Group:		Graphics
Url:		http://jocr.sourceforge.net/
Source0:	http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz
Source1:	http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz.asc
Source2:	%{name}-icons.tar.bz2

BuildRequires:	netpbm-devel
Obsoletes:	%{name}-devel <= 0.48

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files (or PNM from stdin); if
pnm-tools installed and running linux-like system you can also use
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs
a text file.

%prep
%setup -q

%build
# We use -fuse-ld=bfd because gold throws out libnetpbm and libm because they
# aren't actually used.
# This is just to make the check below work -- may want to kick that out...
LDFLAGS="$RPM_OPT_FLAGS -fuse-ld=bfd" %configure2_5x --with-netpbm=%{_prefix}
%make

# NOTE: we apparently need it (BuildRequires), so make sure gocr is
# built against netpbm
ldd src/gocr | grep -q libnetpbm || exit 1

%install
%makeinstall_std

%files -n %{name}
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/{examples.txt,gocr.html,unicode.txt}
%{_bindir}/*
%{_mandir}/man1/*

