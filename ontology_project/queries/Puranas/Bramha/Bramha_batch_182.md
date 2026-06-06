# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Bramha 0.3621)
- **Original**: पड़कर संतम्त हो रहे हैं, माता ! तुम हमारे लिये हुए ऋषि-मुनियोंका विधिवत्‌ स्वागत-सत्कार किया। , शरण हो जाओ। उनमेंसे कुछ लोगोंने गौतमका उपहास करते हुए
- **Translation**: 

---

### Verse 2 (Bramha 0.3622)
- **Original**: सबको शरण देनेवाली गौतमी गज्जा गौतमके पूछा--' बूढ़ी माँ । यह तो बताओ, ये गौतम तुम्हारे
- **Translation**: 

---

### Verse 3 (Bramha 0.3623)
- **Original**: स्तोत्नसे प्रसन्न होकर बोलीं--'ब्रह्मन्‌ू ! तुम मन्त्र पुत्र लगते हैं या पोते? कल्याणी ! सच-सच
- **Translation**: 

---

### Verse 4 (Bramha 0.3624)
- **Original**: पढ़ते हुए मेंर जलसे अपनी पलोका अभिषेक करो। बताना। वृद्ध पुरुषके लिये युवती स्त्री विषके
- **Translation**: 

---

### Verse 5 (Bramha 0.3625)
- **Original**: इससे यह रूपवती हो जायगी। इसके सभी अड्ड समान है और वृद्धा स्त्रीके लिये युवा पुरुष
- **Translation**: 

---

### Verse 6 (Bramha 0.3626)
- **Original**: मनोहर होंगे। नेत्रोंमें भी सुन्दरता आ जायगी तथा अमृतके समान। प्रिय और अप्रियका संयोग हमने
- **Translation**: 

---

### Verse 7 (Bramha 0.3627)
- **Original**: यह सब प्रकारके शुभ लक्षणोंसे शोभा पाने लगेगी।' दीर्घकालके पश्चात्‌ यहीं देखा है।' गौतम और
- **Translation**: 

---

### Verse 8 (Bramha 0.3628)
- **Original**: गड्जाजीके आदेशसे दोनोंने ऐसा ही किया, उनकी पतली दोनों इस परिहासको सुनकर चुप रह
- **Translation**: 

---

### Verse 9 (Bramha 0.3629)
- **Original**: अतः उनकी कृपासे दोनों पति-पत्नी सुन्दर रूपवाले गये। आतिथ्य ग्रहण करके सब महर्षि चले गये।
- **Translation**: 

---

### Verse 10 (Bramha 0.3630)
- **Original**: हों गये। उनके अभिषेकका जो जल था, वह उनकी बातोंकों याद करके ये दोनों दम्पति बहुत
- **Translation**: 

---

### Verse 11 (Bramha 0.3631)
- **Original**: नदीरूपमें परिणत हो गया। वृद्धा नामसे ही उस दुःखी हुए। एक दिन स्त्रीसहित गौतमने मुनिवर
- **Translation**: 

---

### Verse 12 (Bramha 0.3632)
- **Original**: नदीकी ख्याति हुई। गौतमने जो शिवलिम्गकी अगस्त्यजीसे पूछ--“महर्षे ! कौन-सा देश या तीर्थ
- **Translation**: 

---

### Verse 13 (Bramha 0.3633)
- **Original**: स्थापना की, वह भी वृद्धाके ही नामपर “वृद्धेश्वर' ऐसा है, जहाँ जानेसे कल्याणकी प्राप्ति होती है?”
- **Translation**: 

---

### Verse 14 (Bramha 0.3634)
- **Original**: कहलाया। वहीं मुनिश्रेष्ठ गौतमने वृद्धाके साथ पूर्ण अगस्त्थने कहा-ब्रह्मन्‌ू ! मैंने मुनियोंके
- **Translation**: 

---

### Verse 15 (Bramha 0.3635)
- **Original**: आनन्द प्राप्त किया। तबसे उस तीर्थका नाम 'वृद्धा- मुखसे सुना है, गोदावरी नदीमें स्त्रान करनेसे सब
- **Translation**: 

---

### Verse 16 (Bramha 0.3636)
- **Original**: संगम' हो गया। वहाँ किया हुआ स्नान और दान कामनाएँ पूर्ण होती हैं। सब मनोरथोंको सिद्ध करनेवाला है। #>- क/फस्फ2,>
- **Translation**: 

---

### Verse 17 (Bramha 0.3637)
- **Original**: 176 * संक्षिप्त ब्रह्मपुराण * इलातीर्थके आविर्भावकी कथा ब्रह्माजी कहते हैं--इलातीर्थक नामसे जिस
- **Translation**: 

---

### Verse 18 (Bramha 0.3638)
- **Original**: व्यसनमें आसक्त है। यह कैसे ब्रिपत्तिमें फैले--इसके तीर्थकी प्रसिद्धि है, वह मनुष्योंकों सब प्रकारकी [खिि कोई उपाय सोचो। मेरा विचार है कि तुम सिद्धि देनेवाला, ब्रह्महत्या आदि पापोंकों दूर
- **Translation**: 

---

### Verse 19 (Bramha 0.3639)
- **Original**: मनोहर मृगीका रूप धारण करके इसके सामनेसे करनेवाला तथा सम्पूर्ण कामनाओंको पूर्ण करनेवाला
- **Translation**: 

---

### Verse 20 (Bramha 0.3640)
- **Original**: निकलो और इसे अपनी ओर आकृष्ट करके है। बैबस्वत मनुके बंशमें इल नामक एक राजा
- **Translation**: 

---

