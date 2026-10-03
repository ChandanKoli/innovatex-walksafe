import re

with open('src/pages/demo.astro', 'r') as f:
    content = f.read()

# 1. Route Trade-Off Card Wrapper
# We will combine lines 40-41 into one div.
old_wrapper_1 = """            <div class="w-full md:absolute md:top-4 md:left-4 z-[400] md:w-96 flex flex-col gap-4 pointer-events-auto">
                <div class="backdrop-blur-md bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-700 shadow-xl rounded-xl p-5 md:p-6 transition-all">"""
new_wrapper_1 = """            <div class="absolute top-4 left-4 z-[400] w-96 bg-white/95 dark:bg-slate-900/95 backdrop-blur-sm border border-slate-200 dark:border-slate-700 shadow-2xl rounded-xl transition-all p-5 md:p-6 flex flex-col gap-4 pointer-events-auto">"""

if old_wrapper_1 in content:
    content = content.replace(old_wrapper_1, new_wrapper_1)
    # Remove the extra closing div for Top Left Card
    content = content.replace("""                    </div>
                </div>
            </div>""", """                    </div>
            </div>""", 1)

# 2. Report Street Hazard Card Wrapper
old_wrapper_2 = """            <div class="w-full sm:w-auto sm:self-end md:absolute md:bottom-8 md:right-4 z-[400] md:w-80 pointer-events-auto mt-auto">
                <div class="backdrop-blur-md bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-700 shadow-xl rounded-xl p-5 md:p-6 w-full sm:w-[360px] md:w-full transition-all">"""
new_wrapper_2 = """            <div class="absolute bottom-8 right-4 z-[400] w-80 bg-white/95 dark:bg-slate-900/95 backdrop-blur-sm border border-slate-200 dark:border-slate-700 shadow-2xl rounded-xl transition-all p-5 md:p-6 pointer-events-auto mt-auto">"""

if old_wrapper_2 in content:
    content = content.replace(old_wrapper_2, new_wrapper_2)
    # Remove the extra closing div for Hazard Menu
    content = content.replace("""                    </div>
                </div>
            </div>""", """                    </div>
            </div>""", 1)


# 3. Headings
content = content.replace('text-base font-extrabold text-slate-900 dark:text-white', 'text-base text-slate-900 dark:text-white font-bold')
content = content.replace('text-sm font-extrabold text-slate-900 dark:text-white flex items-center', 'text-sm text-slate-900 dark:text-white font-bold flex items-center')

# 3b. Inner labels and secondary text
text_replacements = {
    'text-slate-400 dark:text-slate-500': 'text-slate-600 dark:text-slate-400',
    'text-slate-500 dark:text-slate-400': 'text-slate-600 dark:text-slate-400',
    'text-slate-700 dark:text-slate-300': 'text-slate-600 dark:text-slate-400',
    'text-slate-500 dark:text-slate-300': 'text-slate-600 dark:text-slate-400',
}
for old, new in text_replacements.items():
    content = content.replace(old, new)


# 4. Input Fields
old_select_wrapper = 'class="flex items-center bg-slate-50/50 dark:bg-slate-800/50 border border-slate-200/50 dark:border-slate-700/50 rounded-xl px-3 py-2"'
new_select_wrapper = 'class="w-full bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-white rounded-lg p-2 flex items-center"'
content = content.replace(old_select_wrapper, new_select_wrapper)

with open('src/pages/demo.astro', 'w') as f:
    f.write(content)

print("Modifications done!")
