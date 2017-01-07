#!/bin/bash

# This is needed until we officialy have the lxqt-l10n package

[ ! -z "$!" ] && exit
MODULE="$1"
DIR=$(mktemp -d)
VERSION="0.11.1"

pushd "${DIR}"
git clone https://github.com/lxde/lxqt-l10n --branch 0.11.1
mkdir translations
mv lxqt-l10n/"${MODULE}" translations
tar cfj "${MODULE}"-l10n-${VERSION}.tar.xz translations
popd
mv "${DIR}/${MODULE}-l10n-${VERSION}".tar.xz .
rm -rf "${DIR}"
