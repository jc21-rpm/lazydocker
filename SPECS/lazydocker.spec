%define debug_package %{nil}

%global gh_user     jesseduffield
%global gh_commit   152b36577137fd95f288e12cee5fd6d857a2d101
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_version  0.23.3

# see https://fedoraproject.org/wiki/PackagingDrafts/Go#Build_ID
%global _dwz_low_mem_die_limit 0
%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') " -i -v -x %{?**};
%endif

Name:           lazydocker
Version:        0.23.3
Release:        1%{?dist}
Summary:        A simple terminal UI for both docker and docker-compose, written in Go with the gocui library.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{gh_version}.tar.gz
BuildRequires:  golang

%description
Memorising docker commands is hard. Memorising aliases is slightly less hard. Keeping track of your containers
across multiple terminal windows is near impossible. What if you had all the information you needed in one
terminal window with every common command living one keypress away (and the ability to add custom commands as
well). Lazydocker's goal is to make that dream a reality.

%prep
%setup -qn %{name}-%{gh_version}

%build
%gobuild -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc LICENSE *.md docs/*.md

%changelog
* Tue Jun 25 2024 Jamie Curnow <jc@jc21.com> 0.23.3-1
- v0.23.3

* Thu Mar 25 2021 Jamie Curnow <jc@jc21.com> 0.12.0-1
- v0.12.0

* Mon Nov 16 2020 Jamie Curnow <jc@jc21.com> 0.10.0-1
- v0.10.0

* Mon Jun 1 2020 Jamie Curnow <jc@jc21.com> 0.9.0-1
- v0.9.0

* Mon Feb 3 2020 Jamie Curnow <jc@jc21.com> 0.8.0-1
- v0.8.0

* Mon Nov 18 2019 Jamie Curnow <jc@jc21.com> 0.7.6-1
- v0.7.6

* Tue Nov 12 2019 Jamie Curnow <jc@jc21.com> 0.7.5-1
- v0.7.5

* Mon Sep 9 2019 Jamie Curnow <jc@jc21.com> 0.7.4-1
- v0.7.4

* Mon Aug 26 2019 Jamie Curnow <jc@jc21.com> 0.7.1-1
- v0.7.1

* Thu Aug 15 2019 Jamie Curnow <jc@jc21.com> 0.7.0-1
- v0.7.0

* Mon Aug 5 2019 Jamie Curnow <jc@jc21.com> 0.6.4-1
- v0.6.4

* Tue Jul 30 2019 Jamie Curnow <jc@jc21.com> 0.6.3-1
- v0.6.3

* Fri Jul 5 2019 Jamie Curnow <jc@jc21.com> 0.4.0-1
- v0.4.0

