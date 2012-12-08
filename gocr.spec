%define _disable_ld_as_needed 1

Summary:	OCR (Optical Character Recognition) program
Name:		gocr
Version:	0.49
Release:	%mkrel 1
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




%changelog
* Wed Nov 02 2011 Andrey Bondrov <abondrov@mandriva.org> 0.49-1
+ Revision: 711839
- New version 0.49

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.48-4
+ Revision: 664909
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.48-3mdv2011.0
+ Revision: 605491
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.48-2mdv2010.1
+ Revision: 520428
- use %%define _disable_ld_as_needed 1 due to lack of time fixing it properly
- rebuilt for 2010.1

* Wed Oct 07 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.48-1mdv2010.0
+ Revision: 455643
- Update to 0.48
- Remove the devel provides since no external package uses it and upstream has disabled it

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.45-4mdv2010.0
+ Revision: 425019
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.45-3mdv2009.1
+ Revision: 316750
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.45-2mdv2009.0
+ Revision: 222788
- fix build
- fix build
- fix #%%define is forbidden
- rebuild

  + Guillaume Bedot <littletux@mandriva.org>
    - 0.45

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.44-3mdv2008.1
+ Revision: 171877
- create directory for XDG menu entry
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- rebuild
- auto convert menu to XDG
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu May 17 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.44-1mdv2008.0
+ Revision: 27685
- Updated to 0.44.


* Sun Dec 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.43-1mdv2007.0
+ Revision: 98316
- Import gocr

* Sun Dec 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.43-1mdv2007.1
- 0.43 (#27715)
- drop the overflow patch, it seems fixed differently

* Sun Aug 13 2006 Oden Eriksson <oeriksson@mandriva.org> 0.40-5mdv2007.0
- added a fix segfault for some gray pics (P1)

* Thu Jul 27 2006 Austin Acton <austin@mandriva.org> 0.40-4mdv2007.0
- remove deprecated gtk1.2 frontend
- clean before install

* Mon May 29 2006 Stefan van der Eijk <stefan@eijk.nu> 0.40-3mdk
- %%mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.40-2mdk
- Rebuild

* Fri Apr 22 2005 Marcel Pol <mpol@mandriva.org> 0.40-1mdk
- P1: fix integer and heap overflow

* Wed Feb 16 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.39-2mdk
- add missing includes
- make sure gocr is built against netpbm

* Sat Jun 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.39-1mdk
- 0.39

* Wed Dec 31 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.38-1mdk
- 0.38
- url

