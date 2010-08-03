Name:           supybot-Meetbot
Version:        0.1.4
Release:        %mkrel 1
Summary:        Plugin for Supybot for handling IRC meetings

Group:          Networking/IRC
License:        BSD
URL:            http://wiki.debian.org/MeetBot
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

