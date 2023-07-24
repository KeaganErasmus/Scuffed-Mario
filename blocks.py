from load_assets import *

blocks_sheet = Load_assets("Block.png")

block = blocks_sheet.get_sprites(0, 16, 16, 1)

b_block = blocks_sheet.get_sprites(2, 16, 16, 1)

b_brick = blocks_sheet.get_sprites(4, 16, 16, 1)

brick = blocks_sheet.get_sprites(6, 16, 16, 1)

b_wall = blocks_sheet.get_sprites(8, 16, 16, 1)

solid_wall = blocks_sheet.get_sprites(10, 16, 16, 1)

b_solid_wall = blocks_sheet.get_sprites(12, 16, 16, 1)

y_question = blocks_sheet.get_sprites(14, 16, 16, 1)

b_question = blocks_sheet.get_sprites(16, 16, 16, 1)

r_question = blocks_sheet.get_sprites(18, 16, 16, 1)

w_wall = blocks_sheet.get_sprites(20, 16, 16, 1)

w_solid_wall = blocks_sheet.get_sprites(22, 16, 16, 1)

w_brick_wall = blocks_sheet.get_sprites(24, 16, 16, 1)

w_brick = blocks_sheet.get_sprites(26, 16, 16, 1)

wall = blocks_sheet.get_sprites(28, 16, 16, 1)