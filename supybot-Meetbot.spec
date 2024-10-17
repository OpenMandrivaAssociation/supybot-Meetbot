Name:           supybot-Meetbot
Version:        0.1.4
Release:        3
Summary:        Plugin for Supybot for handling IRC meetings

Group:          Networking/IRC
License:        BSD
URL:            https://wiki.debian.org/MeetBot
Source0:        http://code.zgib.net/tar//MeetBot-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Requires:       supybot
Requires:       python-pygments
Requires:       python-docutils

BuildArch:      noarch
BuildRequires:  python

%description
MeatBot is designed to assist in running meetings, taking notes, and so on. 
It is in pure python, as a plugin to supybot. However, there is a clear 
distinction between meeting-code and IRC-code, so it should be relatively 
easy to port to other bots. It is under the supybot license (3-clause BSD).

%prep
%setup -q -n MeetBot-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/MeetBot
install -pm 644 *.py $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/MeetBot
install -pm 644 *.css $RPM_BUILD_ROOT/%{python_sitelib}/supybot/plugins/MeetBot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt doc/Manual.txt doc/meetingLocalConfig-example.py
%{python_sitelib}/supybot/plugins/MeetBot



%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.1.4-2mdv2011.0
+ Revision: 590101
- rebuild for python 2.7

* Tue Aug 03 2010 Michael Scherer <misc@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 565509
- import supybot-Meetbot


* Tue Aug 03 2010 Michael Scherer <misc@mandriva.org> 0.1.4-1mdv
- adaptation from Fedora

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-3
- Add default css files. 

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-2
- Fix url

* Fri Sep 11 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.4-1
- Update to 0.1.4 release. 

* Sun Aug 23 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.3-1
- Update to 0.1.3 release. 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.2-1
- Update to 0.1.2 release. 

* Tue Jul 07 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.1-2
- Fix install location to be the correct name. 
- Add additional doc files

* Mon Jul 06 2009 Kevin Fenzi <kevin@tummy.com> - 0.1.1-1
- Upgrade to 0.1.1 version

* Sun Jun 14 2009 Kevin Fenzi <kevin@tummy.com> - 0-0.1.20090614darcs
- Initial version for fedora review
