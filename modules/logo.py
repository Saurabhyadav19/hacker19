class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;35m 
                _______  _______  _        _______  _______  __     _____  
      |\     /|(  ___  )(  ____ \| \    /\(  ____ \(  ____ )/  \   / ___ \ 
      | )   ( || (   ) || (    \/|  \  / /| (    \/| (    )|\/) ) ( (   ) )
      | (___) || (___) || |      |  (_/ / | (__    | (____)|  | | ( (___) |
      |  ___  ||  ___  || |      |   _ (  |  __)   |     __)  | |  \____  |
      | (   ) || (   ) || |      |  ( \ \ | (      | (\ (     | |       ) |
      | )   ( || )   ( || (____/\|  /  \ \| (____/\| ) \ \____) (_/\____) )
      |/     \||/     \|(_______/|_/    \/(_______/|/   \__/\____/\______/ \033[1;91mv1.0


\033[1;36m =============================================\033[1;m
\033[1;35m|          Install Best Hacking Tool          |
\033[1;36m =============================================\033[00m''')

  @classmethod
  def tool_footer(self):
    print('''\033[1;36m_______________________________________________
===============================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mWe can't install hacker19.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some error.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[1;35m  [ + ] \033[1;32mUse It At Your Own Risk.
\033[1;35m  [ + ] \033[1;32mNo Warranty.
\033[1;35m  [ + ] \033[1;32mUse it legal purpose only.
\033[1;35m  [ + ] \033[1;32mWe are not responsible for your actions.
\033[1;35m  [ + ] \033[1;32mDo not do things that are forbidden.

\033[1;31m If you are installing this tool.
 that means you are agree with all terms.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[1;35m    [ + ] \033[1;32mhacker19 installed successfully.
\033[1;35m    [ + ] \033[1;32mTo run hacker19.
\033[1;35m    [ + ] \033[1;32mType hacker19 in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[1;35m  [ 1 ] \033[1;32mUpdate your hacker19.
\033[1;35m  [ 0 ] \033[1;32mFor Back.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[1;35m      [ + ] \033[1;32mhacker19 Updated Successfully.
\033[1;35m      [ + ] \033[1;32mPress Enter to continue.\033[00m''')
    self.tool_footer()

  @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mNo network connection?\033[1;m
\033[1;31m  [ + ]  \033[1;31mAre you offline?\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mWe can't Update hacker19.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
\033[1;35m       [+] Tool Name :- \033[1;32mhacker19
\033[1;35m       [+] Author :- \033[1;32mSaurabh Yadav
\033[1;35m       [+] Latest Update :- \033[1;32m27/07/2022.\033[1;m
\033[1;35m       [+] Tools :- \033[1;32mtotal {total} tools.\033[1;m

\033[1;35m [+] \033[1;32mhacker19 is automatic tool installer.
\033[1;35m [+] \033[1;32mMade for termux and linux based system.
\033[1;31m [+] Note :- Use this tool at your own risk.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[01;35m =============================================
\033[01;32m|_____________ Select your tool ______________|
 \033[01;35m=============================================\033[00m""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;35m  [ + ] \033[1;32mSorry ??
\033[1;35m  [ + ] \033[1;37m'{name}'\033[01;32m is already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;35m  [ + ] \033[1;32mInstalled Successfully !!
\033[1;35m  [ + ] \033[1;37m'{name}'\033[01;32m is Installed Successfully !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;35m  [ + ] \033[1;31mSorry ??
\033[1;35m  [ + ] \033[1;37m'{name}'\033[01;31m is not Installed !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\033[01;36m =============================================
\033[01;35m|  00) Back                                   |
 \033[01;36m=============================================\033[00m""")

  @classmethod
  def updating(self):
    print ("""\033[01;35m =============================================
\033[01;32m|______________ Updating hacker19 ______________|
 \033[01;35m=============================================\033[00m""")

  @classmethod
  def installing(self):
    print ("""\033[01;35m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;35m=============================================\033[00m""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;35m  [ 1 ] \033[1;32mShow all tools.\033[1;35m [ \033[1;91mAlmost {total} tools\033[1;35m ]
\033[1;35m  [ 2 ] \033[1;32mTools Category.
\033[1;35m  [ 3 ] \033[1;32mUpdate hacker19.
\033[1;35m  [ 4 ] \033[1;32mAbout Us.
\033[1;35m  [ x ] \033[1;32mFor Exit.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
\033[1;35m         [ + ] \033[1;32mThanks for using hacker19
\033[1;35m         [ + ] \033[1;32mGood By..... :)\033[00m''')
    self.tool_footer()
