from setuptools import setup
import setup_translate

pkg = 'Extensions.EPGTranslator'
setup(name='enigma2-plugin-extensions-epgtranslator',
       version='3.0',
       description='epgtranslator...',
       package_dir={pkg: 'EPGTranslator'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'README', 'LICENSE', 'LICENSE.GPLv2', 'keymap.xml', 'setup.xml', 'pic/*.png', 'pic/buttons/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
