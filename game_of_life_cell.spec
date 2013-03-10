# -*- mode: python -*-

##### include mydir in distribution #######
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas
###########################################




a = Analysis(['.\\..\\..\\github_repos\\a_game_of_life\\game_of_life_cell.py'],
             pathex=['C:\\Users\\beeper\\Projects\\_frameworks_\\pyinstaller-2.0'],
             hiddenimports=[],
             hookspath=None)
			 
			 
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + [('assets\\icon.bmp','.\\..\\..\\github_repos\\a_game_of_life\\assets\\icon.bmp','DATA')],
          name=os.path.join('dist', 'game_of_life_cell.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=False,
		  icon='.\\..\\..\\github_repos\\a_game_of_life\\assets\\icon.ico'		  
		)
app = BUNDLE(exe,
             name=os.path.join('dist', 'game_of_life_cell.exe.app'))
