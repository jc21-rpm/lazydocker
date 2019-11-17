%define debug_package %{nil}

%global gh_user     jesseduffield
%global gh_commit   450d16304087f16da0f9ce15b54640599cb163d6
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_version  0.7.6

# see https://fedoraproject.org/wiki/PackagingDrafts/Go#Build_ID
%global _dwz_low_mem_die_limit 0
%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n') " -i -v -x %{?**};
%endif

Name:           lazydocker
Version:        0.7.6
Release:        1%{?dist}
Summary:        A simple terminal UI for both docker and docker-compose, written in Go with the gocui library.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  golang

%description
Memorising docker commands is hard. Memorising aliases is slightly less hard. Keeping track of your containers
across multiple terminal windows is near impossible. What if you had all the information you needed in one
terminal window with every common command living one keypress away (and the ability to add custom commands as
well). Lazydocker's goal is to make that dream a reality.

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{gh_version}.tar.gz
tar xzf v%{gh_version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
ln -snf %{_builddir}/%{name}-%{gh_version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
export LDFLAGS="${LDFLAGS} -X main.commit=%{gh_short} -X main.date=$(date -u +%Y%m%d.%H%M%%S) -X main.version=%{version}"

%gobuild -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc %{name}-%{gh_version}/LICENSE %{name}-%{gh_version}/*.md %{name}-%{gh_version}/docs/*.md

%changelog
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

