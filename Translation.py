#Translation
import ast
#translations = [("avocado", "e li") , ("bell pepper", "deng long jiao"), ("bitter melon" , "ku gua")]
myfile = open("translation.txt" , "r")
#myfile.write(str(translations))
mystr = myfile.readline()
print(mystr)
translations = ast.literal_eval(mystr)
myfile.close()
def translate():
    a = input("Translation: ")
    matched = False
    for i in translations:
        if i [0] == a:
            print(i[1])
            matched = True
        elif i[1] == a:
            print(i[0])
            matched = True
    if matched == False:       
        newwordChinese = input("There is no definition for this word? What is the Chinese word? ")
        newwordEnglish = a
        newwordpair = (newwordEnglish, newwordChinese)
        print(newwordpair)
        translations.append(newwordpair)
        mysavefile = open("translation.txt","w")
        mystring = str(translations)
        mysavefile.write(mystring)
        mysavefile.close()
    translate()
    
                           
    
translate()

"""
if a ==("avocado"):
    print("鳄梨")
if a==("鳄梨"):
    print("Avocado")
    
if a ==("bell pepper"):
    print("灯笼椒")
if a==("灯笼椒"):
    print("Bell pepper")
    
if a ==("bitter melon"):
    print("苦瓜")
if a==("苦瓜"):
    print("Bitter melon")
    
if a ==("chayote"):
    print("佛手瓜")
if a==("佛手瓜"):
    print("Chayote")
    
if a ==("cucumber"):
    print("黄瓜")
if a==("黄瓜"):
    print("Cucumber")
    
if a ==("ivy gourd"):
    print("红瓜")
if a==("红瓜"):
    print("Ivy gourd")
    
if a ==("eggplant"):
    print("茄子")
if a==("茄子"):
    print("eggplant")
    
if a ==("luffa"):
    print("丝瓜")
if a==("丝瓜"):
    print("Luffa")
 
if a ==("olive fruit"):
    print("橄榄")
if a==("橄榄"):
    print("Olive fruit")
 
if a ==("pumpkin"):
    print("南瓜")
if a==("南瓜"):
    print("Pumpkin")
 
if a ==("pineapple"):
    print("菠萝")
if a==("菠萝"):
    print("Pineapple")
 
if a ==("squash"):
    print("葫芦")
if a==("葫芦"):
    print("Squash")
 
if a ==("sweet pepper"):
    print("甜椒")
if a==("甜椒"):
    print("Sweet pepper ")
 
if a ==("tomato"):
    print("蕃茄")
if a==("蕃茄"):
    print("Tomato")
 
if a ==("vanilla"):
    print("香子兰")
if a==("香子兰"):
    print("Vanilla")
 
if a ==("west Indian gherkin"):
    print("西印度黄瓜")
if a==("西印度黄瓜"):
    print("West Indian gherkin")
 
if a ==("winter melon"):
    print("冬瓜")
if a==("冬瓜"):
    print("Winter melon ")
 
if a ==("zucchini"):
    print("西葫芦")
if a==("西葫芦"):
    print("Zucchini")

if a ==("noodles"):
    print("面条")
if a ==("面条"):
    print("noodles")
    
if a ==("rice"):
    print("米饭")
if a==("米饭"):
    print("rice")
    
if a ==("apple"):
    print("苹果")
if a ==("苹果"):
    print("apple")
     
if a ==("banana"):
    print("香蕉")
if a ==("香蕉"):
    print("banana")
       
if a ==("pear"):
    print("梨子")
if a ==("梨子"):
    print("pear")
     
if a ==("peach"):
    print("桃子")
if a ==("桃子"):
    print("peach")

if a ==("miki"):
    print("I love you")
    """