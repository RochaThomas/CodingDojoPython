
from flask_app import app
from flask import redirect, render_template, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def disp_create_new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    return render_template('create_recipe.html', user_id=user_id)

@app.route('/recipes/<int:recipe_id>')
def disp_one_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_data = {
        'id': recipe_id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('recipe_show.html', user=User.get_user_by_id(user_data), recipe=Recipe.get_one_recipe(recipe_data))

@app.route('/recipes/edit/<int:recipe_id>')
def disp_edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_data = {
        'id': recipe_id
    }
    return render_template('recipe_edit.html', recipe=Recipe.get_one_recipe(recipe_data))

@app.route('/recipes/new/process', methods=['POST'])
def process_new_recipe():
    if not Recipe.is_valid_recipe(request.form):
        return redirect('/recipes/new')
    recipe_id = Recipe.save(request.form)
    return redirect(f"/recipes/{recipe_id}")

@app.route('/recipes/edit/process', methods=['POST'])
def process_edit_recipe():
    print(request.form)
    if not Recipe.is_valid_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")
    Recipe.update_recipe(request.form)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    recipe_data = {
        'id': recipe_id
    }
    Recipe.delete(recipe_data)
    return redirect('/dashboard')