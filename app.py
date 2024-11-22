'''
I developed this program because I wanted to brush up on Python a bit and challenge myself. 
The original goal was to solve 3 problems by creating a CLI, 
but I decided to take a different approach. Of course, 
I used Google Chrome and artificial intelligence for some tasks, but the main work was done by me.
Thank you Nikita Lykyanenko, teacher from university.
'''

from flask import Flask, request, render_template_string, session
import math
import string
import random

app = Flask(__name__)
app.secret_key = 'what_the_price_of_this'

@app.route('/')
def home():
    return render_template_string("""
    <h1>Choose an option (1-20)</h1>
    <form action="/run_option" method="POST">
        <input type="text" name="option" placeholder="Enter a number between 1 and 20" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/run_option', methods=['POST'])
def run_option():
    option = request.form.get('option')

    if option == '1':
        return one()
    elif option == '2':
        return two()
    elif option == '3':
        return three()
    elif option == '4':
        return four()
    elif option == '5':
        return five()
    elif option == '6':
        return six()
    elif option == '7':
        return seven()
    elif option == '8':
        return eight()
    elif option == '9':
        return nine()
    elif option == '10':
        return ten()
    elif option == '11':
        return eleven()
    elif option == '12':
        return twelve()
    elif option == '13':
        return thirteen()
    elif option == '14':
        return fourteen()
    elif option == '15':
        return fifteen()
    elif option == '16':
        return sixteen()
    elif option == '17':
        return seventeen()
    elif option == '18':
        return eighteen()
    elif option == '19':
        return nineteen()
    elif option == '20':
        return twenty()

    return "Something went wrong!"

def one():
    return render_template_string("""
    <h1>Vowel and Consonant Counter</h1>
    <form action="/one" method="POST">
        <input type="text" name="word" placeholder="Enter a word" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/one', methods=['POST'])
def one_post():
    dic_eng = "aeiouAEIOU"
    vowel = 0
    cons = 0
    user_inp = request.form.get('word')

    for char in user_inp:
        if char.isalpha():
            if char.lower() in dic_eng:
                vowel += 1
            else:
                cons += 1
    
    return render_template_string("""
    <h1>Vowel and Consonant Counter</h1>
    <p>Vowels: {{ vowel }}, Consonants: {{ cons }}</p>
    <a href="/">Back to options</a>
    """, vowel=vowel, cons=cons)

def two():
    return render_template_string("""
    <h1>Degrees to DMS Conversion</h1>
    <form action="/two" method="POST">
        <input type="number" name="degree" placeholder="Enter degree" step="any" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/two', methods=['POST'])
def two_post():
    user_degree = float(request.form.get('degree'))
    degrees = int(user_degree)
    decimal_minutes = (user_degree - degrees) * 60
    minutes = int(decimal_minutes)
    seconds = (decimal_minutes - minutes) * 60

    return render_template_string("""
    <h1>Degrees to DMS Conversion</h1>
    <p>{{ degree }}° = {{ degrees }}° {{ minutes }}' {{ seconds }}"</p>
    <a href="/">Back to options</a>
    """, degree=user_degree, degrees=degrees, minutes=minutes, seconds=seconds)

def three():
    return render_template_string("""
    <h1>Geodetic Problem Choice</h1>
    <form action="/three" method="POST">
        <input type="radio" name="choice" value="1" required> 1 - Direct geodetic problem<br>
        <input type="radio" name="choice" value="2" required> 2 - Inverse geodetic problem<br>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/three', methods=['POST'])
def three_post():
    user_choice = int(request.form.get('choice'))
    result = ""
    
    if user_choice == 1:
        result = "Direct geodetic problem"
    elif user_choice == 2:
        result = "Inverse geodetic problem"
    else:
        result = "Invalid choice"
    
    return render_template_string("""
    <h1>Geodetic Problem</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)

def four():
    return render_template_string("""
    <h1>Quadratic Equation Solver</h1>
    <form action="/four" method="POST">
        <input type="number" name="a" placeholder="Enter a" required>
        <input type="number" name="b" placeholder="Enter b" required>
        <input type="number" name="c" placeholder="Enter c" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/four', methods=['POST'])
def four_post():
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    c = float(request.form.get('c'))

    discriminant = b**2 - 4*a*c
    result = ""
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"X1 = {x1}, X2 = {x2}"
    elif discriminant == 0:
        x = -b / (2*a)
        result = f"X = {x}"
    else:
        result = "No real solutions"
    
    return render_template_string("""
    <h1>Quadratic Equation Solution</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)

def five():
    return render_template_string("""
    <h1>Lat to Kir</h1>
    <form action="/five" method="POST">
        <input type="text" name="text" placeholder="Enter text" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/five', methods=['POST'])
def five_post():
    dictionary = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З',
        'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
        'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь'
    }
    user_text = request.form.get('text')
    result = []

    for char in user_text:
        if char in dictionary:
            result.append(dictionary[char])
        else:
            result.append(char)

    return render_template_string("""
    <h1>Lat to Kir</h1>
    <p>Converted text: {{ result }}</p>
    <a href="/">Back to options</a>
    """, result=''.join(result))

def six():
    return render_template_string("""
    <h1>Triangle Existence and Right Triangle Check</h1>
    <form action="/six" method="POST">
        <input type="number" name="a" placeholder="Enter side a" required>
        <input type="number" name="b" placeholder="Enter side b" required>
        <input type="number" name="c" placeholder="Enter side c" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/six', methods=['POST'])
def six_post():
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    c = float(request.form.get('c'))

    if a <= 0 or b <= 0 or c <= 0:
        result = "Triangle doesn't exist."
    elif a + b <= c or a + c <= b or b + c <= a:
        result = "Triangle doesn't exist."
    else:
        a, b, c = sorted([a, b, c])
        if a**2 + b**2 == c**2:
            result = "The triangle is right."
        else:
            result = "The triangle is not right."

    return render_template_string("""
    <h1>Triangle Existence and Right Triangle Check</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)

def seven():
    return render_template_string("""
    <h1>Character Count</h1>
    <form action="/seven" method="POST">
        <input type="text" name="words" placeholder="Enter words" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/seven', methods=['POST'])
def seven_post():
    user_input = request.form.get('words')
    count_dict = {}
    
    for char in user_input:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    result = ""
    for char in user_input:
        if count_dict[char] > 0:
            count = count_dict[char]
            if count > 1:
                result += f"{count}{char}"
            else:
                result += char
            count_dict[char] = 0

    return render_template_string("""
    <h1>Character Count</h1>
    <p>Result: {{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)

def eight():
    return render_template_string("""
    <h1>Even or Odd and Divisibility by 3</h1>
    <form action="/eight" method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/eight', methods=['POST'])
def eight_post():
    user_inp = int(request.form.get('number'))
    digit_sum = sum(int(digit) for digit in str(user_inp))

    result = ""
    if user_inp % 2 == 0:
        result += "The number is even. "
    else:
        result += "The number is odd. "
    
    if digit_sum % 3 == 0:
        result += "The sum of digits is divisible by 3."

    return render_template_string("""
    <h1>Even or Odd and Divisibility by 3</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)

def nine():
    return render_template_string("""
    <h1>Factorial and Subfactorial</h1>
    <form action="/nine" method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/nine', methods=['POST'])
def nine_post():
    n = int(request.form.get('number'))

    fact = math.factorial(n)
    subfact = 0

    if n == 0:
        subfact = 1
    elif n == 1:
        subfact = 0
    else:
        derangement = [0] * (n + 1)
        derangement[0] = 1
        derangement[1] = 0
        
        for i in range(2, n + 1):
            derangement[i] = (i - 1) * (derangement[i - 1] + derangement[i - 2])
        
        subfact = derangement[n]

    return render_template_string("""
    <h1>Factorial and Subfactorial</h1>
    <p>Factorial: {{ fact }}<br>Subfactorial: {{ subfact }}</p>
    <a href="/">Back to options</a>
    """, fact=fact, subfact=subfact)

def ten():
    return render_template_string("""
    <h1>Fibonacci Sequence</h1>
    <form action="/ten" method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/ten', methods=['POST'])
def ten_post():
    user_inp = int(request.form.get('number'))

    if user_inp == 0:
        fib = 0
    elif user_inp == 1:
        fib = 1
    else:
        a, b = 0, 1
        for _ in range(2, user_inp + 1):
            a, b = b, a + b
        fib = b

    return render_template_string("""
    <h1>Fibonacci Sequence</h1>
    <p>Fibonacci number: {{ fib }}</p>
    <a href="/">Back to options</a>
    """, fib=fib)

@app.route('/eleven', methods=['GET', 'POST'])
def eleven():
    if 'bot_number' not in session:
        session['bot_number'] = random.randrange(1, 100)

    result = None
    if request.method == 'POST':
        user_guess = request.form.get('guess')

        if user_guess is None or user_guess.strip() == '':
            result = "Please enter a number between 1 and 100."
        else:
            try:
                user_guess = int(user_guess)
            except ValueError:
                result = "Please enter a valid number"
            else:
                bot_number = session['bot_number']

                if user_guess < bot_number:
                    result = "Higher!"
                elif user_guess > bot_number:
                    result = "Lower!"
                else:
                    result = f"Congratulations! The number was {bot_number}."
                    session.pop('bot_number', None)

    return render_template_string("""
    <h1>Guess the Number</h1>
    {% if result %}
        <p>{{ result }}</p>
    {% endif %}
    <form action="/eleven" method="POST">
        <input type="number" name="guess" placeholder="Enter a number between 1 and 100" required>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Back to options</a>
    """, result=result)

def twelve():
    return render_template_string("""
    <h1>Decimal and Binary Conversion</h1>
    <form action="/twelve" method="POST">
        <label>Choice:</label>
        <input type="radio" name="choice" value="1"> Decimal to Binary
        <input type="radio" name="choice" value="2"> Binary to Decimal
        <br>
        <input type="text" name="number" placeholder="Enter number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/twelve', methods=['POST'])
def twelve_post():
    user_choice = request.form.get('choice')
    user_input = request.form.get('number')

    if user_choice == '1':
        result = bin(int(user_input))[2:]
        return render_template_string("""
        <h1>Decimal to Binary</h1>
        <p>Binary number: {{ result }}</p>
        <a href="/">Back to options</a>
        """, result=result)
    
    elif user_choice == '2':
        result = int(user_input, 2)
        return render_template_string("""
        <h1>Binary to Decimal</h1>
        <p>Decimal number: {{ result }}</p>
        <a href="/">Back to options</a>
        """, result=result)

    return render_template_string("""
    <h1>Decimal and Binary Conversion</h1>
    <p>Error: Please select a valid option.</p>
    <a href="/">Back to options</a>
    """)

def thirteen():
    return render_template_string("""
    <h1>Leap Year Check</h1>
    <form action="/thirteen" method="POST">
        <input type="number" name="year" placeholder="Enter a year" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/thirteen', methods=['POST'])
def thirteen_post():
    user_inp = int(request.form.get('year'))

    if (user_inp % 4 == 0 and user_inp % 100 != 0) or (user_inp % 400 == 0):
        result = f"{user_inp} is a leap year!"
    else:
        result = f"{user_inp} is not a leap year!"

    return render_template_string("""
    <h1>Leap Year Check</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)

def fifteen():
    return render_template_string("""
    <h1>Arabic to Roman and Roman to Arabic Conversion</h1>
    <form action="/fifteen" method="POST">
        <label>Choice:</label>
        <input type="radio" name="choice" value="1"> Arabic to Roman
        <input type="radio" name="choice" value="2"> Roman to Arabic
        <br>
        <input type="text" name="number" placeholder="Enter a number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/fifteen', methods=['POST'])
def fifteen_post():
    user_choice = request.form.get('choice')
    user_input = request.form.get('number')

    if user_choice == '1':
        arabic_num = int(user_input)
        if arabic_num < 1 or arabic_num > 3999:
            result = "The number must be between 1 and 3999"
        else:
            val = [
                1000, 900, 500, 400, 100, 90, 50, 40,
                10, 9, 5, 4, 1
            ]
            syb = [
                "M", "CM", "D", "CD", "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"
            ]
            roman_numeral = ''
            i = 0
            while arabic_num > 0:
                for _ in range(arabic_num // val[i]):
                    roman_numeral += syb[i]
                    arabic_num -= val[i]
                i += 1
            result = f"Roman number: {roman_numeral}"

    elif user_choice == '2':
        roman_num = user_input.upper()
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        arabic_value = 0
        prev_value = 0
        for char in reversed(roman_num):
            current_value = roman_dict.get(char, 0)
            if current_value == 0:
                result = f"Error! The char: '{char}' isn't roman style"
                break
            if current_value < prev_value:
                arabic_value -= current_value
            else:
                arabic_value += current_value
            prev_value = current_value
        else:
            result = f"Arabic number: {arabic_value}"

    else:
        result = "Invalid option."

    return render_template_string("""
    <h1>Arabic to Roman and Roman to Arabic Conversion</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)


def sixteen():
    return render_template_string("""
    <h1>Caesar Cipher</h1>
    <form action="/sixteen" method="POST">
        <label>Choice:</label>
        <input type="radio" name="choice" value="1"> Encrypt
        <input type="radio" name="choice" value="2"> Decrypt
        <br>
        <input type="text" name="text" placeholder="Enter text" required>
        <input type="number" name="shift" placeholder="Enter shift value" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/sixteen', methods=['POST'])
def sixteen_post():
    user_choice = request.form.get('choice')
    text = request.form.get('text')
    shift = int(request.form.get('shift'))

    result = ""
    if user_choice == '2':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            result += char

    return render_template_string("""
    <h1>Caesar Cipher</h1>
    <p>Result: {{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)


def seventeen():
    return render_template_string("""
    <h1>Perfect Number Check</h1>
    <form action="/seventeen" method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/seventeen', methods=['POST'])
def seventeen_post():
    user_inp = int(request.form.get('number'))

    if user_inp <= 1:
        result = "The number isn't perfect"
    else:
        divisor_sum = sum(i for i in range(1, user_inp) if user_inp % i == 0)
        result = f"The number {user_inp} is perfect? - {divisor_sum == user_inp}"

    return render_template_string("""
    <h1>Perfect Number Check</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)


def eighteen():
    return render_template_string("""
    <h1>GCD and LCM Calculation</h1>
    <form action="/eighteen" method="POST">
        <input type="number" name="a" placeholder="Enter number a" required>
        <input type="number" name="b" placeholder="Enter number b" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/eighteen', methods=['POST'])
def eighteen_post():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))

    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd

    result = f"GCD is {gcd}, LCM is {lcm}"

    return render_template_string("""
    <h1>GCD and LCM Calculation</h1>
    <p>{{ result }}</p>
    <a href="/">Back to options</a>
    """, result=result)


def nineteen():
    return render_template_string("""
    <h1>Prime Numbers</h1>
    <form action="/nineteen" method="POST">
        <input type="number" name="number" placeholder="Enter a number" required>
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/nineteen', methods=['POST'])
def nineteen_post():
    user_input = int(request.form.get('number'))
    primes = []

    for num in range(2, user_input + 1):
        is_prime = True

        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return render_template_string("""
    <h1>Prime Numbers</h1>
    <p>All primes: {{ primes }}</p>
    <a href="/">Back to options</a>
    """, primes=primes)


@app.route('/twenty', methods=['GET', 'POST'])
def twenty():
    if 'bot_number' not in session:
        session['bot_number'] = ''.join(random.sample('0123456789', 4))
        session['attempts'] = 0

    result = None
    if request.method == 'POST':
        user_inp = request.form.get('guess')

        if user_inp is None or len(user_inp) == 0:
            result = "Please enter a 4-digit number with no repeating digits."
        elif len(user_inp) != 4 or not user_inp.isdigit() or len(set(user_inp)) != 4:
            result = "Please enter a valid 4-digit number with no repeating digits."
        else:
            bot_number = session['bot_number']
            bulls = sum(1 for i in range(4) if user_inp[i] == bot_number[i])
            cows = sum(1 for i in range(4) if user_inp[i] != bot_number[i] and user_inp[i] in bot_number)

            session['attempts'] += 1
            attempts = session['attempts']

            if bulls == 4:
                result = f"Congratulations! You've guessed the number {bot_number} in {attempts} attempts."
                session.pop('bot_number', None)
                session.pop('attempts', None)
            else:
                result = f"Bulls: {bulls}, Cows: {cows} (Attempts: {attempts})"
    
    return render_template_string("""
    <h1>Bulls and Cows Game</h1>
    <p>{{ result }}</p>
    <form action="/twenty" method="POST">
        <input type="text" name="guess" placeholder="Enter a 4-digit number" required>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Back to options</a>
    """, result=result)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()

