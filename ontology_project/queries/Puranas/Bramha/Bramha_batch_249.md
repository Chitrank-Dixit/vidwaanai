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

### Verse 1 (Bramha 0.4961)
- **Original**: आकाशवाणीसे कहा--' बिना पशुके यह यज्ञ पूर्ण वे जो कुछ भी कहें, वही करो।' नहीं हो सकता।' उत्तर मिला--'पुरुषसूक्तसे तदनन्तर इतिहास, पुराण तथा अन्य जो भो
- **Translation**: 

---

### Verse 2 (Bramha 0.4962)
- **Original**: परमपुरुषको स्तुति करो।' बाड्मय शास्त्र है, वह मेरे मुखमें स्वतः आ गया
- **Translation**: 

---

### Verse 3 (Bramha 0.4963)
- **Original**: “बहुत अच्छा'--कहकर मैंने अपने जन्मदाता
- **Translation**: 

---

### Verse 4 (Bramha 0.4964)
- **Original**: * कुशतर्पश एवं प्रणीता-संगम-तीर्थकी महिमा * रडर देवाधि जनार्दनका भक्तिपूर्वक पुरुषसूक्तके मन्त्रोंद्रार
- **Translation**: 

---

### Verse 5 (Bramha 0.4965)
- **Original**: हों। उस यज्ञमें मन्त्रोंद्वारा मैंने प्रणीतापात्रका भी स्तवन किया। उस समय फिर आकाशवाणी
- **Translation**: 

---

### Verse 6 (Bramha 0.4966)
- **Original**: सम्पादन किया था। वह प्रणीताका जल ही हुई-'ब्रह्मन्‌! तुम मुझे ही पशु बनाओ।' मैं
- **Translation**: 

---

### Verse 7 (Bramha 0.4967)
- **Original**: प्रणीता नदीके रूपमें परिणत हुआ। फिर कुशोंसे समझ गया, ये मेरे जन्मदाता अविनाशी पुरुष हैं।
- **Translation**: 

---

### Verse 8 (Bramha 0.4968)
- **Original**: मार्जत करके प्रणीताका मैंने विसर्जन कर दिया। मैंने त्रिगुणमयी डोरियोंसे कालयूपके पार्श्रभागमें
- **Translation**: 

---

### Verse 9 (Bramha 0.4969)
- **Original**: मार्जज करते समय जो प्रणीताके जलकी बूँदे उन्हें बाँध दिया। सबसे पहले प्रकट हुए पुरुषरूपी
- **Translation**: 

---

### Verse 10 (Bramha 0.4970)
- **Original**: इधर-उधर गिरी, बे गुणवान्‌ तोर्थोंके रूपमें पशुका, जो कुशॉपर विराजमान थे, प्रोक्षण किया।
- **Translation**: 

---

### Verse 11 (Bramha 0.4971)
- **Original**: प्रकट हुईं। वे तीर्थ स्नान करनेसे यज्ञके फल इसी समय पुरुषसे ये सब वस्तुएँ प्रकट हुईं--उनके
- **Translation**: 

---

### Verse 12 (Bramha 0.4972)
- **Original**: देनेवाले हैं। देवाधिदेव भगवान्‌ विष्णुने जिसे सदा मुखसे ब्राह्मण, भुजाओंसे क्षत्रिय, मुखसे इन्द्र और
- **Translation**: 

---

### Verse 13 (Bramha 0.4973)
- **Original**: सुशोभित किया है, वह गौतमी बैकुण्ठ धामपर अग्नि, प्राणसे वायु, कानसे दिशाएँ तथा मस्तकसे
- **Translation**: 

---

### Verse 14 (Bramha 0.4974)
- **Original**: पहुँचनेके लिये सीढ़ियॉंकी पंक्ति है। संमार्जन सम्पूर्ण स्वर्गलोककी उत्पत्ति हुई। मनसे चन्द्रमा, करनेके बाद जहाँ कुश इस पृथ्वीपर गिरे थे, वह नेज्रसे सूर्य, नाभिसे अन्तरिक्ष, दोनों जाँघोंसे वैश्य
- **Translation**: 

---

### Verse 15 (Bramha 0.4975)
- **Original**: स्थान कुशतर्पण नामक तीर्थ हुआ, जो बहुत और चरणोंसे शुद्र तथा पृथ्वीका प्राकट्य हुआ।
- **Translation**: 

---

### Verse 16 (Bramha 0.4976)
- **Original**: पुण्यफल देनेवाला है। मैंने विन्ध्यपर्वतके उत्तर रोमकूृपोंसे ऋषि और केशोंसे ओषधियाँ प्रकट
- **Translation**: 

---

### Verse 17 (Bramha 0.4977)
- **Original**: जहाँ यूप खड़ा किया था, वह स्थान भगवान्‌ हुईं। नखोंसे ग्रामीण तथा जंगली पशु हुए। पायु
- **Translation**: 

---

### Verse 18 (Bramha 0.4978)
- **Original**: विष्णुका आश्रय बना तथा वह यूप अक्षयवटके और उपस्थसे कृमि, कीट एवं पतड़र आदिका
- **Translation**: 

---

### Verse 19 (Bramha 0.4979)
- **Original**: रूपमें परिणत हुआ। वह वृक्ष नित्य एवं कालस्वरूप जन्म हुआ। इनके सिवा जो कुछ भी स्थावर-
- **Translation**: 

---

### Verse 20 (Bramha 0.4980)
- **Original**: है और स्मरण करनेमात्रसे यज्ञका पुण्य देनेवाला जज्गम तथा दृश्य-अदृश्य जगत्‌ है, वह सब
- **Translation**: 

---

