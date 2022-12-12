# add and delete data in dictionary
user_info = {'name' : 'Nishant',
'age': 19,
'fav_movie':['ramlila','salamat','man'],
'fav_tunes': ['awaking','fairly tale']
}

user_info['fav_song'] = ['song1', 'song2']
print(user_info)

#pop

popped_item=user_info.pop('fav_tunes')
print(f"popped item is {popped_item}")
print(user_info)