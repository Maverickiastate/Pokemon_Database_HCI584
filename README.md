# Pokemon DataScience project for HCI584

## Read me
### Here are a few examples of some of the things one can do with the data in this project. 

#### First user case scenario: Fastest fire type. 
#### The first line will take the data and create a dataframe where only pokemon that have fire as a type 1 or 2 typing. The next query will that that dataframe and elminate any that have a speed stat lower than 100. The next line will sort from fastest to slowest. Finally the table is displayed and the top result of that table is also displayed with that pokemon's full data.
    fast_fire = df.query("type_1 == 'Fire' or type_2 == 'Fire'")
    most_fast = fast_fire.query("speed > 100")
    final_fast = most_fast.sort_values(by="speed", ascending=False)
    display(final_fast[['name', 'type_1', 'type_2','speed']])
    display(final_fast.iloc[0])

#### Second user case scenario: Finding the pokemon with the best defenseive stats (must be a normal status pokemon)
#### This scenario follows along a similar structure to the first example but here a new column is being created. In this scenario maybe you want to find the Pokemon with the highest collective defensive stats. You add the columns together and create a new one. The process afterwards, again, is similar to the mechanics of the first example.
    df['total_defense'] = (df['hp'] + df['defense'] + df['sp_defense'])
    normal_status = df.query("status == 'Normal'")
    total_def = normal_status.sort_values(by="total_defense", ascending=False)
    display(total_def[['pokedex_number','name', 'total_defense', 'hp', 'defense', 'sp_defense']].head(20))
    display(total_def.iloc[0])

#### Third user case scenario: Using a move dictionary to find pokemon based off move data.
#### Example 1: This function returns true/false when you search for a pokemon with moves you would like it to know. For example you could search that Gloom knows Charm, Flash, Snore and it would return True

    def check_pokemon_moves(p, move_list, move_dict):

        if move_dict.get(p) == None:
            return None

        moves = move_dict[p]
        for move in move_list:
            if move not in moves: return False

        return True
    tests
    print(check_pokemon_moves("Pokemokee", ["charm", "flash", "snore"], move_dict)) # None
    print(check_pokemon_moves("Gloom", ["charm", "flash", "snore"], move_dict)) # True
    print(check_pokemon_moves("Gloom", ["charm", "flash", "frizzle-frazzle"], move_dict)) # True

#### Example 2: This function returns an integer when you search for a pokemon with moves you would like it to know. For example you could search that Gloom knows Charm, Flash, Snore and it would return 3
    def has_pokemon_moves(p, move_list, move_dict):

        if move_dict.get(p) == None:
            return None
        
        num_moves = 0

        moves = move_dict[p]
        for move in move_list:
            if move in moves: 
                num_moves += 1

        return num_moves

    Tests
    print(has_pokemon_moves("Pokemokee", ["charm", "flash", "snore"], move_dict)) # None
    print(has_pokemon_moves("Gloom", ["charm", "flash", "snore"], move_dict)) # 3
    print(has_pokemon_moves("Gloom", ["charm", "flash", "frizzle-frazzle"], move_dict)) # 2

#### Example 3: This function returns lists of pokemon when you search for a move(s) you would like it to know. For example you could search Charm, Flash, Snore and it would return Gloom plus any other Pokemon that know the move
    def which_pokemon_have_moves(move_list, move_dict):
        found_pokemons = []
        
        for p in move_dict:
            if check_pokemon_moves(p, move_list, move_dict) == True:
                found_pokemons.append(p)
    
        return found_pokemons

    Tests
    print(which_pokemon_have_moves(["charm", "flash", "snore", "aromatherapy"], move_dict)) #Vileplume, Petilil, Lilligant...
    print(which_pokemon_have_moves(["charm", "flash", "frizzle-frazzle"], move_dict)) #None