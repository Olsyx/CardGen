from src.HtmlGenerator import *
from src.Fonts import *

from PIL import ImageFont
import re
import os

class Style:

    symbol = ""    # Only for text markers
    display = ""   # block, inline, etc.

    # Flex Container
    flex_direction = ""
    flex_wrap = ""
    flex_flow = ""
    justify_content = ""
    align_items = ""
    align_content = ""
    gap = ""
    row_gap = ""
    column_gap = ""

    # Flex Children
    flex_order = ""
    flex_grow = ""
    flex_shrink = ""
    flex_basis = ""
    align_self = ""

    # Content
    margin = ""
    margin_top = ""
    margin_left = ""
    margin_right = ""
    margin_bottom = ""

    padding = ""
    padding_top = ""
    padding_left = ""
    padding_right = ""
    padding_bottom = ""

    background_image = ""
    background_color = ""

    # Tables
    border = ""
    border_collapse = ""
    border_radius = ""
    border_style = ""
    border_color = ""
    border_top = ""
    border_left = ""
    border_right = ""
    border_bottom = ""
    
    # Position and Size
    position = ""
    position_x = "" 
    position_y = ""     

    width = ""          
    height = ""         
    max_width = ""      
    max_height = ""    
    min_width = ""      
    min_height = ""     

    expanded_x = ""
    expanded_y = ""
    expanded_width = "" 
    expanded_height = ""

    image_width = ""  
    image_height = "" 
    
    # Transforms
    flip = ""           # Horizontal / Vertical / Both
    rotate = ""         # Degrees
    scale = ""          # X Y

    # Custom Transforms
    deform = ""         # Arc
    deform_radius = ""
    deform_degrees = ""

    # Filters and visual modifiers
    mix_blend_mode = "" # https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode
    blur = ""
    brightness = ""
    contrast = ""
    drop_shadow = ""
    grayscale = ""
    hue_rotate = ""
    invert = ""
    opacity = ""
    saturate = ""
    sepia = ""
    
    # Text properties
    alignment = ""
    font = ""
    font_size = ""
    font_style = ""
    font_weight = ""
    text_color = ""
    text_decorations = ""
    line_height = ""
    letter_spacing = ""
    text_transform = ""

    # Debug
    debug_color = ""


    # -------------- FUNCTIONS -------------- #

    def __init__(self, structure):
        
        self.symbol = structure.get("symbol")
        self.display = structure.get("display")
        
        # Flex Container
        self.flex_direction = structure.get("flex-direction")
        self.flex_wrap = structure.get("flex-wrap")
        self.flex_flow = structure.get("flex-flow")
        self.justify_content = structure.get("justify-content")
        self.align_items = structure.get("align-items")
        self.align_content = structure.get("align-content")
        self.gap = structure.get("gap")
        self.row_gap = structure.get("row-gap")
        self.column_gap = structure.get("column-gap")

        # Flex Children
        self.flex_order = structure.get("flex-order")
        self.flex_grow = structure.get("flex-grow")
        self.flex_shrink = structure.get("flex-shrink")
        self.flex_basis = structure.get("flex-basis")
        self.align_self = structure.get("align-self")

        # Content
        self.margin = structure.get("margin")
        self.margin_top = structure.get("margin-top")
        self.margin_left = structure.get("margin-left")
        self.margin_right = structure.get("margin-right")
        self.margin_bottom = structure.get("margin-bottom")

        self.padding = structure.get("padding")
        self.padding_top = structure.get("padding-top")
        self.padding_left = structure.get("padding-left")
        self.padding_right = structure.get("padding-right")
        self.padding_bottom = structure.get("padding-bottom")

        self.background_image = structure.get("background-image")
        self.background_color = structure.get("background-color")
        
        # Borders
        self.border = structure.get("border")
        self.border_collapse = structure.get("border-collapse")
        self.border_radius = structure.get("border-radius")
        self.border_style = structure.get("border-style")
        self.border_color = structure.get("border-color")
        self.border_top = structure.get("border-top")
        self.border_left = structure.get("border-left")
        self.border_right = structure.get("border-right")
        self.border_bottom = structure.get("border-bottom")

        # Position and Size
        self.position_x = structure.get("x")
        self.position_y = structure.get("y")
        
        self.width = structure.get("width")
        self.height = structure.get("height")
        self.max_width = structure.get("max-width")
        self.max_height = structure.get("max-height")
        self.min_width = structure.get("min-width")
        self.min_height = structure.get("min-height")
        
        self.expanded_x = structure.get("expanded-x")
        self.expanded_y = structure.get("expanded-y")
        self.expanded_width = structure.get("expanded-width")
        self.expanded_height = structure.get("expanded-height")

        self.image_width = structure.get("img-width")
        self.image_height = structure.get("img-height")

        # Transforms
        self.flip = structure.get("flip")
        self.rotate = structure.get("rotate")
        self.scale = structure.get("scale")
        
        # Custom Transforms
        self.deform = structure.get("deform")
        self.deform_degrees = structure.get("deform-degrees")
        self.deform_radius = structure.get("deform-radius")

        # Filters and visual modifiers
        self.mix_blend_mode = structure.get("mix-blend-mode")
        self.blur = structure.get("blur")
        self.brightness = structure.get("brightness")
        self.contrast = structure.get("contrast")
        self.drop_shadow = structure.get("drop-shadow")
        self.grayscale = structure.get("grayscale")
        self.hue_rotate = structure.get("hue-rotate")
        self.invert = structure.get("invert")
        self.opacity = structure.get("opacity")
        self.saturate = structure.get("saturate")
        self.sepia = structure.get("sepia")

        # Text properties
        self.alignment = structure.get("alignment")
        self.font = structure.get("font")
        self.font_size = structure.get("font-size")
        self.font_style = structure.get("font-style")
        self.font_weight = structure.get("font-weight")
        self.text_color = structure.get("text-color")
        self.text_decorations = structure.get("text-decorations")
        self.line_height = structure.get("line-height")
        self.letter_spacing = structure.get("letter-spacing")
        self.text_transform = structure.get("text-transform")

        # Debug
        self.debug_color = structure.get("debug-color")

    def add(self, other_style): 

        # self.symbo -- No need modificating
        self.display = self.decide_attribute(self.display, other_style.display)

        # Flex Container
        self.flex_direction = self.decide_attribute(self.flex_direction, other_style.flex_direction)
        self.flex_wrap = self.decide_attribute(self.flex_wrap, other_style.flex_wrap)
        self.flex_flow = self.decide_attribute(self.flex_flow, other_style.flex_flow)
        self.justify_content = self.decide_attribute(self.justify_content, other_style.justify_content)
        self.align_items = self.decide_attribute(self.align_items, other_style.align_items)
        self.align_content = self.decide_attribute(self.align_content, other_style.align_content)
        self.gap = self.decide_attribute(self.gap, other_style.gap)
        self.row_gap = self.decide_attribute(self.row_gap, other_style.row_gap)
        self.column_gap = self.decide_attribute(self.column_gap, other_style.column_gap)

        # Flex Children
        self.flex_order = self.decide_attribute(self.flex_order, other_style.flex_order)
        self.flex_grow = self.decide_attribute(self.flex_grow, other_style.flex_grow)
        self.flex_shrink = self.decide_attribute(self.flex_shrink, other_style.flex_shrink)
        self.flex_basis = self.decide_attribute(self.flex_basis, other_style.flex_basis)
        self.align_self = self.decide_attribute(self.align_self, other_style.align_self)

        # Content
        self.margin = self.decide_attribute(self.margin, other_style.margin)
        self.margin_top = self.decide_attribute(self.margin_top, other_style.margin_top)
        self.margin_left = self.decide_attribute(self.margin_left, other_style.margin_left)
        self.margin_right = self.decide_attribute(self.margin_right, other_style.margin_right)
        self.margin_bottom = self.decide_attribute(self.margin_bottom, other_style.margin_bottom)

        self.padding = self.decide_attribute(self.padding, other_style.padding)
        self.padding_top = self.decide_attribute(self.padding_top, other_style.padding_top)
        self.padding_left = self.decide_attribute(self.padding_left, other_style.padding_left)
        self.padding_right = self.decide_attribute(self.padding_right, other_style.padding_right)
        self.padding_bottom = self.decide_attribute(self.padding_bottom, other_style.padding_bottom)

        self.background_image = self.decide_attribute(self.background_image, other_style.background_image)
        self.background_color = self.decide_attribute(self.background_color, other_style.background_color)

        # Tables
        self.border = self.decide_attribute(self.border, other_style.border)
        self.border_collapse = self.decide_attribute(self.border_collapse, other_style.border_collapse)
        self.border_radius = self.decide_attribute(self.border_radius, other_style.border_radius)
        self.border_style = self.decide_attribute(self.border_style, other_style.border_style)
        self.border_color = self.decide_attribute(self.border_color, other_style.border_color)
        self.border_top = self.decide_attribute(self.border_top, other_style.border_top)
        self.border_left = self.decide_attribute(self.border_left, other_style.border_left)
        self.border_right = self.decide_attribute(self.border_right, other_style.border_right)
        self.border_bottom = self.decide_attribute(self.border_bottom, other_style.border_bottom)
        
        # Position and Size
        self.position = self.decide_attribute(self.position, other_style.position) 
        self.position_x = self.decide_attribute(self.position_x, other_style.position_x) 
        self.position_y = self.decide_attribute(self.position_y, other_style.position_y)     

        self.width = self.decide_attribute(self.width, other_style.width)   
        self.height = self.decide_attribute(self.height, other_style.height)
        self.max_width = self.decide_attribute(self.max_width, other_style.max_width)      
        self.max_height = self.decide_attribute(self.max_height, other_style.max_height)    
        self.min_width = self.decide_attribute(self.min_width, other_style.min_width)      
        self.min_height = self.decide_attribute(self.min_height, other_style.min_height)     

        self.expanded_x = self.decide_attribute(self.expanded_x, other_style.expanded_x)
        self.expanded_y = self.decide_attribute(self.expanded_y, other_style.expanded_y)
        self.expanded_width = self.decide_attribute(self.expanded_width, other_style.expanded_width) 
        self.expanded_height = self.decide_attribute(self.expanded_height, other_style.expanded_height)

        self.image_width = self.decide_attribute(self.image_width, other_style.image_width)  
        self.image_height = self.decide_attribute(self.image_height, other_style.image_height) 
        
        # Transforms
        self.flip = self.decide_attribute(self.flip, other_style.flip)          
        self.rotate = self.decide_attribute(self.rotate, other_style.rotate)        
        self.scale = self.decide_attribute(self.scale, other_style.scale)        

        # Custom Transforms
        self.deform = self.decide_attribute(self.deform, other_style.deform)            
        self.deform_degrees = self.decide_attribute(self.deform_degrees, other_style.deform_degrees)        
        self.deform_radius = self.decide_attribute(self.deform_radius, other_style.deform_radius)          

        # Filters and visual modifiers
        self.mix_blend_mode = self.decide_attribute(self.mix_blend_mode, other_style.mix_blend_mode) # https://developer.mozilla.org/en-US/docs/Web/CSS/mix-blend-mode
        self.blur = self.decide_attribute(self.blur, other_style.blur)
        self.brightness = self.decide_attribute(self.brightness, other_style.brightness)
        self.contrast = self.decide_attribute(self.contrast, other_style.contrast)
        self.drop_shadow = self.decide_attribute(self.drop_shadow, other_style.drop_shadow)
        self.grayscale = self.decide_attribute(self.grayscale, other_style.grayscale)
        self.hue_rotate = self.decide_attribute(self.hue_rotate, other_style.hue_rotate)
        self.invert = self.decide_attribute(self.invert, other_style.invert)
        self.opacity = self.decide_attribute(self.opacity, other_style.opacity)
        self.saturate = self.decide_attribute(self.saturate, other_style.saturate)
        self.sepia = self.decide_attribute(self.sepia, other_style.sepia)
        
        # Text properties
        self.alignment = self.decide_attribute(self.alignment, other_style.alignment) 
        self.font = self.decide_attribute(self.font, other_style.font)
        self.font_size = self.decide_attribute(self.font_size, other_style.font_size)
        self.font_style = self.decide_attribute(self.font_style, other_style.font_style)
        self.font_weight = self.decide_attribute(self.font_weight, other_style.font_weight)
        self.text_color = self.decide_attribute(self.text_color, other_style.text_color)
        self.text_decorations = self.decide_attribute(self.text_decorations, other_style.text_decorations)
        self.line_height = self.decide_attribute(self.line_height, other_style.line_height)
        self.letter_spacing = self.decide_attribute(self.letter_spacing, other_style.letter_spacing)
        self.text_transform = self.decide_attribute(self.text_transform, other_style.text_transform)

        # Debug
        self.debug_color = self.decide_attribute(self.debug_color, other_style.debug_color)

    def is_empty(self):
        return (self.display is None
        
        # Flex Container
        and self.flex_direction is None
        and self.flex_wrap is None
        and self.flex_flow is None
        and self.justify_content is None
        and self.align_items is None
        and self.align_content is None
        and self.gap is None
        and self.row_gap is None
        and self.column_gap is None

        # Flex Children
        and self.flex_order is None
        and self.flex_grow is None
        and self.flex_shrink is None
        and self.flex_basis is None
        and self.align_self is None

        # Content
        and self.margin is None
        and self.margin_top is None
        and self.margin_left is None
        and self.margin_right is None
        and self.margin_bottom is None

        and self.padding is None
        and self.padding_top is None
        and self.padding_left is None
        and self.padding_right is None
        and self.padding_bottom is None

        and self.background_image is None
        and self.background_color is None
        
        # Borders
        and self.border is None
        and self.border_collapse is None
        and self.border_radius is None
        and self.border_style is None
        and self.border_color is None
        and self.border_top is None
        and self.border_left is None
        and self.border_right is None
        and self.border_bottom is None

        # Position and Size
        and self.position_x is None
        and self.position_y is None
        
        and self.width is None
        and self.height is None
        and self.max_width is None
        and self.max_height is None
        and self.min_width is None
        and self.min_height is None
        
        and self.expanded_x is None
        and self.expanded_y is None
        and self.expanded_width is None
        and self.expanded_height is None

        and self.image_width is None
        and self.image_height is None

        # Transforms
        and self.flip is None
        and self.rotate is None
        and self.scale is None
        
        # Custom Transforms
        and self.deform is None
        and self.deform_degrees is None
        and self.deform_radius is None

        # Filters and visual modifiers
        and self.mix_blend_mode is None
        and self.blur is None
        and self.brightness is None
        and self.contrast is None
        and self.drop_shadow is None
        and self.grayscale is None
        and self.hue_rotate is None
        and self.invert is None
        and self.opacity is None
        and self.saturate is None
        and self.sepia is None

        # Text properties
        and self.alignment is None
        and self.font is None
        and self.font_size is None
        and self.font_style is None
        and self.font_weight is None
        and self.text_color is None
        and self.text_decorations is None
        and self.line_height is None
        and self.letter_spacing is None
        and self.text_transform is None

        # Debug
        and self.debug_color is None)

    def decide_attribute(self, original, overwrite):
        if overwrite is None or overwrite == "":
            return original
        
        if original is None:
            return overwrite

        modifier = overwrite[0]
        if modifier != "+" and modifier != "-":
            return overwrite

        overwrite = overwrite.replace("+", "") # if modifier was -, overwrite_value is negative anyway
        overwrite_value, overwrite_unit = self.extract_value_unit(overwrite)
        if overwrite_unit != "":
            return overwrite # There is a unit, so it's a whole number and not an operation

        original_value, original_unit = self.extract_value_unit(original)

        # if modifier was -, overwrite_value is negative anyway
        return str(original_value + overwrite_value) + original_unit # ignore new units

    def get_css(self, expanded=False, debug=False):
        styling = self.get_position(expanded)
        styling += self.get_flex_container()
        styling += self.get_flex_item()
        styling += self.get_dimensions(expanded)
        styling += self.get_margins()
        styling += self.get_paddings()
        styling += self.get_transforms()
        styling += self.get_mix_blend_mode()
        styling += self.get_filter()
        styling += self.get_background(debug)
        styling += self.get_border()
        styling += self.get_text_style()
        styling += self.get_alignment()

        return styling

    def get_adaptive_img_css(self):
        style = ""

        if self.image_width is not None:
            style = "\twidth: " + self.image_width + ";\n"
        else: 
            style = "\twidth: 100%;\n"

        if self.image_height is not None:
            style = "\theight: " + self.image_height + ";\n"
        else: 
            style = "\theight: 100%;\n"

        style += "\tmargin: auto;\n"
        style += "\toverflow: auto;\n"
        return style

    def get_position(self, expanded=False):
        if self.position_x is None and self.position_y is None:
            self.position = "relative"
            return "\tposition: " + self.position + ";\n"

        if self.position == "":
            self.position = "absolute"

        style = "\tposition: " + self.position + ";\n"
        if not expanded or self.expanded_x is None:
            style += self.get_style("left", self.position_x, "mm")
        else:
            style += self.get_style("left", self.expanded_x, "mm")

        if not expanded or self.expanded_y is None:
            style += self.get_style("top", self.position_y, "mm")
        else:
            style += self.get_style("top", self.expanded_y, "mm")

        return style
        
    def get_flex_container(self):
        style = ""

        if self.flex_direction is not None:
            style += "\tflex-direction: " + self.flex_direction +";\n"
            
        if self.flex_wrap is not None:
            style += "\tflex-wrap: " + self.flex_wrap +";\n"
            
        if self.flex_flow is not None:
            style += "\tflex-flow: " + self.flex_flow +";\n"
            
        if self.justify_content is not None:
            style += "\tjustify-content: " + self.justify_content +";\n"
            
        if self.align_items is not None:
            style += "\talign-items: " + self.align_items +";\n"
            
        if self.align_content is not None:
            style += "\talign-content: " + self.align_content +";\n"
            
        if self.gap is not None:
            style += "\tgap: " + self.gap +";\n"
            
        if self.row_gap is not None:
            style += "\trow-gap: " + self.row_gap +";\n"
            
        if self.column_gap is not None:
            style += "\tcolumn_gap: " + self.column_gap +";\n"

        return style
    
    def get_flex_item(self):
        style = ""
            
        if self.flex_order is not None:
            style += "\tflex-order: " + self.flex_order +";\n"

            
        if self.flex_grow is not None:
            style += "\tflex-grow: " + self.flex_grow +";\n"

            
        if self.flex_shrink is not None:
            style += "\tflex-shrink: " + self.flex_shrink +";\n"

            
        if self.flex_basis is not None:
            style += "\tflex-basis: " + self.flex_basis +";\n"

            
        if self.align_self is not None:
            style += "\talign-self: " + self.align_self +";\n"

        return style

    def get_dimensions(self, expanded=False):
        style = ""

        # -- WIDTH --
        if expanded and self.expanded_width is not None:
            style += self.get_size_style("width", self.expanded_width, "mm", self.expanded_height)
        elif self.width is not None:
            style += self.get_size_style("width", self.width, "mm", self.height)

        if self.max_width is not None:
            style += self.get_size_style("max-width", self.max_width, "mm", self.max_height)
            
        if self.min_width is not None:
            style += self.get_size_style("min-width", self.min_width, "mm", self.min_height)
        # ------------
            
        # -- HEIGHT --
        if expanded and self.expanded_height is not None:
            style += self.get_size_style("height", self.expanded_height, "mm", self.expanded_width)
        elif self.height is not None:
            style += self.get_size_style("height", self.height, "mm", self.width)
            
        if self.max_height is not None:
            style += self.get_size_style("max-height", self.max_height, "mm", self.max_width)
            
        if self.min_height is not None:
            style += self.get_size_style("min-height", self.min_height, "mm", self.min_width)
        # ------------

        return style
 
    def get_margins(self):
        style = ""

        if self.margin is not None:
            style += self.get_style("margin", self.margin, "mm")

        if self.margin_top is not None:
            style += self.get_style("margin-top", self.margin_top, "mm")

        if self.margin_left is not None:
            style += self.get_style("margin-left", self.margin_left, "mm")

        if self.margin_right is not None:
            style += self.get_style("margin-right", self.margin_right, "mm")

        if self.margin_bottom is not None:
            style += self.get_style("margin-bottom", self.margin_bottom, "mm")

        return style

    def get_paddings(self):
        style = ""
        if self.padding is not None:
            style += "\tpadding: " + self.padding +";\n"

        if self.padding_top is not None:
            style += "\tpadding-top: " + self.padding_top +";\n"

        if self.padding_left is not None:
            style += "\tpadding-left: " + self.padding_left +";\n"

        if self.padding_right is not None:
            style += "\tpadding-right: " + self.padding_right +";\n"

        if self.padding_bottom is not None:
            style += "\tpadding-bottom: " + self.padding_bottom +";\n"

        return style

    def get_transforms(self):
        if not self.flip and not self.rotate:
            return ""
        
        webkit = "\t-webkit-transform:"
        moz = "\t-moz-transform:"
        o = "\t-o-transform:"
        ms = "\t-ms-transform:"
        transform = "\ttransform:"

        if self.flip:
            flip_op = ""
            self.flip = self.flip.lower()

            if self.flip == "horizontal" or self.flip == "h": flip_op = " scale(-1, 1)"
            elif self.flip == "vertical" or self.flip == "v": flip_op += " scale(1, -1)"
            elif self.flip == "both" or self.flip == "b": flip_op += "scale(-1, -1)"

            webkit += flip_op
            moz += flip_op
            o += flip_op
            ms += flip_op
            transform += flip_op

        if self.scale:
            scale_op = " scale(" + self.scale + ")"
            
            webkit += scale_op
            moz += scale_op
            o += scale_op
            ms += scale_op
            transform += scale_op

        if self.rotate:
            rotate_op = " rotate(" + self.rotate + "deg)"
            
            webkit += rotate_op
            moz += rotate_op
            o += rotate_op
            ms += rotate_op
            transform += rotate_op

        return webkit + ";\n" + moz + ";\n" + o + ";\n" + ms + ";\n" + transform + ";\n"

    def get_mix_blend_mode(self):
        if not self.mix_blend_mode:
            return ""
        
        return "\tmix-blend-mode: " + self.mix_blend_mode + ";\n"

    def get_filter(self):
        style = "\tfilter:"

        applied_filter = False
        
        if self.blur:
            applied_filter = True
            style += " blur(" + self.blur + "px)"
        
        if self.brightness:
            applied_filter = True
            style += " brightness(" + self.brightness + "%)"
        
        if self.contrast:
            applied_filter = True
            style += " contrast(" + self.contrast + "%)"
        
        if self.drop_shadow:
            applied_filter = True
            style += " drop-shadow(" + self.drop_shadow + ")"
        
        if self.grayscale:
            applied_filter = True
            style += " grayscale(" + self.grayscale + "%)"
        
        if self.hue_rotate:
            applied_filter = True
            style += " hue-rotate(" + self.hue_rotate + "deg)"

        if self.invert:
            applied_filter = True
            style += " invert(" + self.invert + "%)"

        if self.opacity:
            applied_filter = True
            style += " opacity(" + self.opacity + "%)"

        if self.saturate:
            applied_filter = True
            style += " saturate(" + self.saturate + "%)"

        if self.sepia:
            applied_filter = True
            style += " sepia(" + self.sepia + "%)"

        if not applied_filter:
            return ""

        return style + ";"

    def get_background(self, debug=False):
        style = "\toverflow: hidden;\n"
        if self.background_image is not None:
            style += '\tbackground-image: url("' + self.background_image + '");\n'
            style += '\tbackground-position: center;\n'
            style += '\tbackground-repeat: no-repeat;\n'
            style += '\tbackground-size: cover;\n'

        if not debug and self.background_color is not None:
            style += "\tbackground-color: " + self.background_color + ";\n"
        elif debug and self.debug_color is not None:
            style += "\tbackground-color: " + self.debug_color + ";\n"
        return style

    def get_border(self):
        style = ""

        if self.border is not None:
            style += "\tborder: " + self.border + ";\n"

        if self.border_radius is not None:
            style +=  self.get_style("border-radius", self.border_radius, "px")

        if self.border_collapse is not None:
            style += "\tborder-collapse: " + self.border_collapse + ";\n"

        if self.border_style is not None:
            style += "\tborder-style: " + self.border_style + ";\n"

        if self.border_color is not None:
            style += "\tborder-color: " + self.border_color + ";\n"
            
        if self.border_top is not None:
            style += "\tborder-top: " + self.border_top + ";\n"
            
        if self.border_left is not None:
            style += "\tborder-left: " + self.border_left + ";\n"
            
        if self.border_right is not None:
            style += "\tborder-right: " + self.border_right + ";\n"
            
        if self.border_bottom is not None:
            style += "\tborder-bottom: " + self.border_bottom + ";\n"

        return style
    
    def get_text_style(self):
        style = ""
        style += self.get_style("font-family", self.font)
        style += self.get_style("font-style", self.font_style)
        style += self.get_style("font-size", self.font_size, "px")
        style += self.get_style("font-weight", self.font_weight)
        style += self.get_style("color", self.text_color)
        style += self.get_style("text-decoration", self.text_decorations)
        style += self.get_style("text-decoration-skip-ink", "auto")
        style += self.get_style("line-height", self.line_height)
        style += self.get_style("letter-spacing", self.letter_spacing)
        style += self.get_style("text-transform", self.text_transform)
        return style

    def get_alignment(self):
        if not self.display:
            style = ""
        else:
            style = "\tdisplay: " + self.display + ";\n"

        if self.alignment is None:
            return style

        data = self.alignment.split(" ")
        for d in data:
            style += self.parse_alignment(d)

        return style 

    def parse_alignment(self, align):
        if self.display != "flex":
            if align == "left" or align == "center" or align == "right":
                return "\ttext-align: " + align + ";\n"

            elif align == "top" or align == "middle" or align == "bottom":
                return "\tvertical-align: " + align + ";\n"
                
        else:    # Text needs to be Flexy for vertical adjustment. It sucks, I know.        
            if align == "left":
                return "\tjustify-content: start;\n"
            
            elif align == "center":
                return "\tjustify-content: center;\n"
                
            elif align == "right":
                return "\tjustify-content: end;\n"

            elif align == "top":
                return "\talign-items: self-start;\n"
                
            elif align == "middle":
                return "\talign-items: center;\n"

            elif align == "bottom":
                return "\talign-items: self-end;\n"

    def get_style(self, tag, value, default_unit=""):
        if value is None:
            return ""
        
        if value[-1].isdigit():
            return "\t" + tag + ": " + value + default_unit + ";\n"
        else:
            return "\t" + tag + ": " + value + ";\n"
        
    def get_size_style(self, tag, value, default_unit, compare_against):
        value = self.get_size_against_proportion(value, compare_against)
        if value is None:
            return ""
        
        return self.get_style(tag, value, default_unit)
        
    def get_size_against_proportion(self, og_value, against_value):
        if og_value is None:
            return None
        
        if ':' not in og_value:
            return og_value
    
        if against_value is None:
            return None
        
        fractions = og_value.split(':')
        proportion = float(fractions[0])/float(fractions[1])

        value, unit = self.extract_value_unit(against_value)
        final_value = str(value * proportion) + unit

        return final_value

    def extract_value_unit(self, original):
        value = re.findall(r"[-+]?(?:\d*\.*\d+)", original)[0] # get all digits (numbers) including floats
        unit = original.replace(value, "") # extract unit as str
        return float(value), unit


    # ---------- DEFORMS ---------- #

    def generate_span_deforms(self, style_class, content):
        if content == "":
            return 
        
        if self.deform == "arc":
            self.generate_arc(style_class, content)

    def generate_arc(self, style_class, content):
        total_degrees, degrees_unit = self.extract_value_unit(self.deform_degrees)
        if total_degrees == 0:
            return
        
        font_url = Fonts.get_url(self.font)
        image_font = ImageFont.truetype(os.path.abspath("./" + font_url), float(self.font_size))
        biggest_width = 0
        for char in content:
            width = image_font.getlength(char)
            if width > biggest_width:
                biggest_width = width
        
        root_css = "\tposition: absolute;\n" 
        root_css += "\ttext-align: center;\n"
        root_css += "\twidth: " + str(biggest_width) + "px;\n" 
        root_css += self.get_style("height", self.deform_radius, "mm")


        invert = 1
        total_degrees = total_degrees
        if total_degrees < 0:
            invert = -1
            total_degrees = -total_degrees
            root_css += "\tdisplay: flex;\n"
            root_css += "\ttransform-origin: top center;\n"
            root_css += "\talign-items: self-end;\n"
            root_css += "\tjustify-content: center;\n"
        else:
            root_css += "\ttransform-origin: bottom center;\n"

        # Center in div
        x = "0"
        y = "0"
        if self.width != None and self.width != "" and self.height != None and self.height != "":
            radius_value, radius_unit = self.extract_value_unit(self.deform_radius)
            
            box_width = self.get_size_against_proportion(self.width, self.height)
            box_height = self.get_size_against_proportion(self.height, self.width)

            box_width_value, box_width_unit = self.extract_value_unit(box_width)
            box_height_value, box_height_unit = self.extract_value_unit(box_height)

            pixel_2_mms = 0.2645833333 # https://www.unitconverters.net/typography/pixel-x-to-millimeter.htm
            char_width_pixels = biggest_width * pixel_2_mms

            if radius_unit == "px": 
                radius_value *= pixel_2_mms

            x = str(box_width_value / 2 - char_width_pixels / 2) + box_width_unit
            
            if invert < 0:
                y = str(box_height_value / 2) + box_height_unit
            else:
                y = str(box_height_value / 2 - radius_value) + box_height_unit


        root_css += self.get_style("top", y, "mm")
        root_css += self.get_style("left", x, "mm")
        HtmlGenerator.store_style(style_class + " span", root_css)

        pixel_degrees = 0.02 # between 0.01 and 0.03 according to https://osdoc.cogsci.nl/3.3/visualangle/#:~:text=Note%20that%20a%20single%20visual,0.01%20to%200.03%20visual%20degrees.
        content_pixels = image_font.getlength(content)

        degrees_so_far = 0

        for index in range(0, len(content)):
            
            char_pixels = image_font.getlength(content[index])
            char_degrees = char_pixels * total_degrees / content_pixels

            char_css = 'transform: rotate(' + str(invert * (degrees_so_far + char_degrees / 2)) + 'deg);'
            HtmlGenerator.store_style(style_class + " .char" + str(index), char_css)

            degrees_so_far += char_degrees

