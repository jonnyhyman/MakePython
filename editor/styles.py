"""
    This file is part of MakePython.
    MakePython is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    HDCS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with HDCS.  If not, see <http://www.gnu.org/licenses/>.
"""

syntax_colors = {
    0:{ # dark syntax theme
        'default' :('#abb2bf'),
        'keyword' :('#c678dd',),
        'builtins':('#56B6C2',),
        'operator':('#c678dd','bold'),
        'brace'   :('#abb2bf',),
        'brace_h' :('#568AF2','bold'),
        'defclass':('#61afef',),
        'string'  :('#98c379',),
        'string2' :('#98c379',),
        'comment' :('#5a6370','italic'),
        'self'    :('#e06c75',),
        'numbers' :('#d19a64',),
    },
    1:{ # light syntax theme
        'default' :('black'),
        'keyword' :('#0023A4',),
        'builtins':('#56B6C2',),
        'operator':('#D77915','bold'),
        'brace'   :('#25193E',),
        'brace_h' :('#568AF2','bold'),
        'defclass':('#D77915','bold'),
        'string'  :('#AF7F2C',),
        'string2' :('#AF7F2C',),
        'comment' :('#486CF0','italic'),
        'self'    :('#40710B','bold'),
        'numbers' :('#0033F0',),
        },
}

ui_colors = {

    0:{ # dark syntax theme
        'bg_window'  :'#21252b',
        'bg_pip_a'   :'0.8',
        'bg_textEdit':'#282c34',
        'py_color'   :'white',
        'bg_button'  :'transparent',
        'bd_button'  :'2px solid white',
      },
    1:{ # light syntax theme
        'bg_window'  :'#f0f0f0',
        'bg_pip_a'   :'0.8',
        'bg_textEdit':'white',
        'py_color'   :'#0023a4',
        'bg_button'  :'#0023a4',
        'bd_button'  :'0px solid white',
      }

}
