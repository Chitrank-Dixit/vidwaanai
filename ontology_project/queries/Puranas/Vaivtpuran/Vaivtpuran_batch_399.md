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

### Verse 1 (Vaivtpuran 21.3704)
- **Original**: »प्रकृतिखण्ड « 165 58%4%$%#%#9 44888 4 45 84 ## 8 $ 4 4 #5 44444 544 #4 4 अ3 कर #क शक फ़भ्कअकक्क डक हक बऊ आफ कक भ्रक अक अक कब मे तुम निरामय गोलोक-धाममें तुलसीकी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 21.3705)
- **Original**: चिहसे रहित श्याम पाषाणकों भगवान्‌ “राघवेन्द्र' अधिष्ठात्री देवी बनकर मेरे स्वरूपभूत श्रीकृष्णके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 21.3706)
- **Original**: का विग्रह मानना चाहिये। जिसमें बहुत छोटे दो साथ निरन्तर क्रीड़ा करोगी। तुम्हारी देहसे उत्पन्न
- **Translation**: 

---

### Verse 4 (Vaivtpuran 21.3707)
- **Original**: चक्रके चिह्न हों, उस नवोन मेघके समान कृष्णवर्णके नदीकी जो अधिष्ठात्री देवी है, वह भारतवर्षमें पाषाणकों भगवान्‌ “दधिवामन' मानना चाहिये, परम पुण्यदा नदी बनकर मेरे अंशभूत क्षार-
- **Translation**: 

---

### Verse 5 (Vaivtpuran 21.3708)
- **Original**: बह गृहस्थोंके लिये सुखदायक है। अत्यन्त छोटे .... होगी। स्वयं तुम महासाध्वी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 21.3709)
- **Original**: आकारमें दो चक्र एवं वनमालासे सुशोभित तुलसीरूपसे बैकुण्ठमें मेरे संनिकट निवास
- **Translation**: 

---

### Verse 7 (Vaivtpuran 21.3710)
- **Original**: पाषाण स्वयं भगवान्‌ 'श्रीधर' का रूप है--ऐसा करोगी। वहाँ तुम लक्ष्मीके समान सम्मानित
- **Translation**: 

---

### Verse 8 (Vaivtpuran 21.3711)
- **Original**: समझना चाहिये। ऐसी मूर्ति भी गृहस्थोंको सदा होओगी। गोलोकके रासमें भी तुम्हारी उपस्थिति
- **Translation**: 

---

### Verse 9 (Vaivtpuran 21.3712)
- **Original**: श्रीसम्पन्न बनाती है। जो पूरा स्थूल हो, जिसकी होगी, इसमें संशय नहीं है। आकृति गोल हो, जिसके ऊपर वनमालाका चिह्न मैं तुम्हारे शापको सत्य करनेके लिये भारतवर्षमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 21.3713)
- **Original**: अद्धित न हो तथा जिसमें दो अत्यन्त स्पष्ट चक्रके *पाषाण' (शालग्राम) बनकर रहूँगा। गण्डकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 21.3714)
- **Original**: चिह्न दिखायो पड़ते हों, उस शालग्राम शिलाकी नदीके तटपर मेरा वास होगा। वहाँ रहनेवाले
- **Translation**: 

---

### Verse 12 (Vaivtpuran 21.3715)
- **Original**: 'दामोदर' संज्ञा है। जो मध्यम श्रेणीका वर्तुलाकार करोड़ों कीड़े अपने तीखे दाँतरूपी आयुधोंसे
- **Translation**: 

---

### Verse 13 (Vaivtpuran 21.3716)
- **Original**: हो, जिसमें दो चक्र तथा तरकस और बाणके काट-काटकर उस पाषाणमें मेरे चक्रका चिह्न
- **Translation**: 

---

### Verse 14 (Vaivtpuran 21.3717)
- **Original**: चिह्न शोभा पाते हों, एवं जिसके ऊपर बाणसे कट करेंगे। जिसमें एक द्वारका चिह्न होगा, चार चक्र
- **Translation**: 

---

### Verse 15 (Vaivtpuran 21.3718)
- **Original**: जानेका चिह्न हो, उस पाषाणको रणमें शोभा होंगे और जो बनमालासे विभूषित होगा, वह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 21.3719)
- **Original**: पानेवाले भगवान्‌ 'रणराम' की संज्ञा देनी चाहिये। नवीन मेघके समान श्यामवर्णका पाषाण “लक्ष्मी-
- **Translation**: 

---

### Verse 17 (Vaivtpuran 21.3720)
- **Original**: जो मध्यम श्रेणीका पाषाण सात चक्रोंसे तथा छत्र नारायण' का बोधक होगा। जिसमें एक द्वार और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 21.3721)
- **Original**: एवं तरकससे अलंकृत हो, उसे भगवान्‌ चार चक्रके चिह्न होंगे तथा वनमालाकी रेखा नहीं
- **Translation**: 

---

### Verse 19 (Vaivtpuran 21.3722)
- **Original**: “राजराजेश्वर 'की प्रतिमा समझे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 21.3723)
- **Original**: उसकी उपासनासे प्रतीत होती होगी, ऐसे नवीन मेघकी तुलना
- **Translation**: 

---

