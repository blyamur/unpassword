# Copyright original theme © 2021 rdbende <rdbende@gmail.com>
# Copyright © 2021 Mons <mons@mons.ws>

package require Tk 8.6

namespace eval ttk::theme::spring-drops-light {
    variable version 1.0
    package provide ttk::theme::spring-drops-light $version

    ttk::style theme create spring-drops-light -parent clam -settings {
        proc load_images {imgdir} {
            variable images
            foreach file [glob -directory $imgdir *.png] {
                set images([file tail [file rootname $file]]) \
                [image create photo -file $file -format png]
            }
        }

        load_images [file join [file dirname [info script]] light]

        array set colors {
            -fg             "#DCEEFF"
            -bg             "#0C6FCC"
            -disabledfg     "#CACACA"
            -selectfg       "#ffffff"
            -selectbg       "#2f60d8"
        }
        ttk::style layout Accent.TButton {
            AccentButton.button -children {
                AccentButton.padding -children {
                    AccentButton.label -side left -expand 1
                } 
            }
        }
        ttk::style layout Switch.TCheckbutton {
            Switch.button -children {
                Switch.padding -children {
                    Switch.indicator -side left
                    Switch.label -side right -expand 1
                }
            }
        }
        ttk::style layout TLabelframe {
            Labelframe.border {
                Labelframe.padding -expand 1 -children {
                    Labelframe.label -side left
                }
            }
        }
        # Accent.TButton
        ttk::style configure Accent.TButton -padding {10 8} -anchor center -foreground #1259B3

        ttk::style map Accent.TButton -foreground \
            [list disabled #1259B3 \
                pressed #FFF]

        ttk::style element create AccentButton.button image \
            [list $images(button-accent-rest) \
                {selected disabled} $images(button-accent-disabled) \
                disabled $images(button-accent-disabled) \
                selected $images(button-accent-rest) \
                pressed $images(button-accent-pressed) \
                active $images(button-accent-hover) \
            ] -border 4 -sticky nsew


        # Switch.TCheckbutton
        ttk::style element create Switch.indicator image \
            [list $images(switch-off-rest) \
                {selected disabled} $images(switch-on-disabled) \
                disabled $images(switch-off-disabled) \
                {pressed selected} $images(switch-on-pressed) \
                {active selected} $images(switch-on-hover) \
                selected $images(switch-on-rest) \
                {pressed !selected} $images(switch-off-pressed) \
                active $images(switch-off-hover) \
            ] -width 46 -sticky w

        # Labelframe
        ttk::style element create Labelframe.border image $images(card) \
            -border 5 -padding 4 -sticky nsew
        
   
    }
}