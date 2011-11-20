%define _disable_ld_as_needed 1

Summary:	OCR (Optical Character Recognition) program
Name:		gocr
Version:	0.49
Release:	%mkrel 2
License:	GPLv2
Group:		Graphics
URL:		http://jocr.sourceforge.net/
Source0:	http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz
Source1:	http://www-e.uni-magdeburg.de/jschulen/ocr/gocr-%{version}.tar.gz.asc
Source2:	%{name}-icons.tar.bz2
#Patch0:	gocr-0.39-includes.patch
BuildRequires:	libnetpbm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

Obsoletes:	%{name}-devel <= 0.48

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files (or PNM from stdin); if
pnm-tools installed and running linux-like system you can also use
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs
a text file.

#%package -n	%{name}-devel
#Summary:	Development tools for gocr
#Group:		Development/C

#%description -n	%{name}-devel
#GOCR is an optical character recognition program, released under the
#GNU General Public License. It reads images in many formats (pnm, pbm,
#pgm, ppm, some pcx and tga image files (or PNM from stdin); if
#pnm-tools installed and running linux-like system you can also use
#pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs
#a text file.

#If you want to develop programs which will manipulate gocr, you should 
#install gocr-devel.  You'll also need to install the gocr package.

#%package -n %{name}-gtk
#Summary:	Gtk+ frontend for gocr
#Group: 		Graphics
#Requires:	%{name} = %{version}
#BuildRequires:  gtk+1.2-devel 

#%description -n %{name}-gtk
#GOCR is an optical character recognition program, released under the
#GNU General Public License. It reads images in many formats (pnm, pbm,
#pgm, ppm, some pcx and tga image files (or PNM from stdin); if
#pnm-tools installed and running linux-like system you can also use
#pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs
#a text file.

#Gtk+-based frontend for gocr.
	
%prep
%setup -q
#patch0 -p1 -b .includes

%build
%configure2_5x
%make

# NOTE: we apparently need it (BuildRequires), so make sure gocr is
# built against netpbm
ldd src/gocr | grep -q libnetpbm || exit 1

#cd frontend/gnome
#%%configure --prefix=%{_xprefix} --bindir=%{_xbindir}
#%%make 

%install
rm -rf %{buildroot}

%makeinstall_std

#ln -sf gnome/mkinstalldirs frontend/mkinstalldirs
#make -C frontend/gnome install DESTDIR=%buildroot

# Menu
#mkdir -p %{buildroot}/{%{_miconsdir},%{_liconsdir},%{_menudir}}
#bzcat %{SOURCE2}|tar xf - -C %buildroot/%{_datadir}

mkdir -p %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}-gtk.desktop
[Desktop Entry]
Type=Application
Exec=%{_xbindir}/gtk-ocr
Icon=%{name}
Categories=Graphics;Viewer;
Name=Gtk-ocr
Comment=Gtk-ocr is a gtk frontend for gocr
EOF

#%post -n %name-gtk
#%{update_menus}
   
#%postun -n %name-gtk
#%{clean_menus}
   
%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(-, root, root)
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/{examples.txt,gocr.html,unicode.txt}
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/mandriva-%{name}-gtk.desktop

#%files -n %{name}-devel
#%defattr(-, root, root)
#%doc AUTHORS
#%{_libdir}/libPgm2asc.a
#%{_includedir}/gocr.h

#%files -n %{name}-gtk
#%defattr(-, root, root)
#%doc frontend/gnome/{AUTHORS,README,TODO}
#%{_menudir}/*
#%{_iconsdir}/*
#%attr(755,root,root) %{_xbindir}/*


