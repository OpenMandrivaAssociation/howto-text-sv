%define format	text-sv
%define format2	TEXT/sv
%define	format3 text

%define version 2006
%define release %mkrel 6

Summary:	HOWTO documents (%{format3} format) from the Linux Documentation Project
Name:		howto-%{format}
Version: 	%version
Release: 	%release
Group:		Books/Howtos
Source0:	howto-text-sv.tar.bz2
Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/howto-%{format}-root
BuildArchitectures: noarch
Requires:   locales-sv howto-utils
BuildRequires:  howto-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

Install this package if you'd like to be able to access the Linux
HOWTO documentation from your own system.

%prep 
rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
cd $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
bzcat %{SOURCE0} | tar xv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2006-6mdv2011.0
+ Revision: 619483
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2006-5mdv2010.0
+ Revision: 429463
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2006-4mdv2009.0
+ Revision: 247033
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2006-3mdv2009.0
+ Revision: 239620
- rebuild
- better description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2006-1mdv2008.1
+ Revision: 126832
- kill re-definition of %%buildroot on Pixel's request
- import howto-text-sv


* Thu Dec 15 2005 Lenny Cartier <lenny@mandriva.com> 2006-1mdk
- rebuild

* Thu Oct 09 2003  Lenny Cartier <lenny@mandrakesoft.com> 9.2-1mdk
- updated

* Sat Sep 14 2002  Lenny Cartier <lenny@mandrakesoft.com> 9.0-1mdk
- update

* Thu Sep 06 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Updated: Thu Sep 06 2001
- Add Require on locale-sv

* Thu Mar 22 2001 Lenny Cartier <lenny@mandrakesoft.com> 8.0-1mdk
- rebuild

* Fri Sep 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.2-1mdk
- bm

* Thu May 09 2000 David BAUDENS <baudens@mandrakesoft.com> 7.1-1mdk
- Update for 7.1 (20000509)

* Fri Jan 07 2000 - David BAUDENS <baudens@mandrakesoft.com>
- Build for 7.0

* Tue Dec 30 1999 - David BAUDENS <baudens@mandrakesoft.com>
- French HTML version

* Sat Dec 04 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 19991204
- Keep only html format (others are in contribs)

* Fri May 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- no <BASE HREF...> in howto-index.html

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Jan 26 1999 Cristian Gafton <gafton@redhat.com>
- updated howtos
- marked translations with %%lang(XX)
- get rid of pdf, ps and dvi formats

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- added the Serbian Howtos

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- updated archive
- added croatian and slovenian subpackages

* Wed Apr 15 1998 Cristian Gafton <gafton@redhat.com>
- updated archive
- subpackages for each language

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- fixed missing HOWTOs because the download ran out of space
- added an index html page for the howto-html package

* Thu Oct 23 1997 Otto Hammersmith <otto@redhat.com>
- untarred the html tarballs to obsolete the ldp package

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed description for the right date

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Sat Apr 19 1997 Otto Hammersmith <otto@redhat.com>
- Updated to more recent HOWTOs.
- In the next major version, /usr/doc really ought to be cleaned out.
  Right now, the ldp and howto packages overlap somewhat. (HTML docs,
  the former, however, only has tar.gz files)
  I didn't want to rearrange too much for 4.2, and there are other
  documentation issues such as /usr/info.

