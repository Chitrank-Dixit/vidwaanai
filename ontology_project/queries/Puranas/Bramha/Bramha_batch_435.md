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

### Verse 1 (Bramha 0.8681)
- **Original**: एक दिन कहते हैं। इसीको कल्प समझो। दिनके संसारमें नहीं आता? तथा क्षर पदार्थ क्या है,
- **Translation**: 

---

### Verse 2 (Bramha 0.8682)
- **Original**: हो बराबर ब्रह्माजीकी रात्रि भी होती है, जिसके जिसको जाननेपर भी आवागमन बना रहता है?
- **Translation**: 

---

### Verse 3 (Bramha 0.8683)
- **Original**: अन्तमें वे सोकर उठते हैं और इस विशाल क्षः और अक्षरके स्वरूपको स्पष्टरूपसे जाननेके
- **Translation**: 

---

### Verse 4 (Bramha 0.8684)
- **Original**: विश्वकी सृष्टि करते हैं। वे यद्यपि निराकार हैं तो लिये हम आपसे यह प्रश्न करते हैं।
- **Translation**: 

---

### Verse 5 (Bramha 0.8685)
- **Original**: भी साकार जगत्‌की रचना करते हैं। उनमें व्यासजीने कहा--मुनिवरो ! इस विषयमें राजा
- **Translation**: 

---

### Verse 6 (Bramha 0.8686)
- **Original**: अणिमा, लघधिमा तथा प्राप्ति आदि शक्तियोंका करालजनक और वसिष्ठके संवादरूप एक प्राचीन
- **Translation**: 

---

### Verse 7 (Bramha 0.8687)
- **Original**: स्वाभाविक निवास है। वे अविनाशी ज्योतिर्मय इतिहासका वर्णन करता हूँ। एक समयको बात
- **Translation**: 

---

### Verse 8 (Bramha 0.8688)
- **Original**: परमेश्वर हैं। उनके सब ओर हाथ-पैर हैं, सब है, सूर्यके समान तेजस्वी मुनिवर बसिष्ठ अपने ओर नेत्र, मस्तक और मुख हैं तथा सब ओर आश्रमपर विराजमान थे। वे परमात्मतत्त्वके प्रतिपादनमें
- **Translation**: 

---

### Verse 9 (Bramha 0.8689)
- **Original**: कान हैं। वे संसारमें सबको व्याप्त करके स्थित कुशल थे । उन्हें अध्यात्मतत्वका निश्चयात्मक ज्ञान
- **Translation**: 

---

### Verse 10 (Bramha 0.8690)
- **Original**: हैं। वे ही भगवान्‌ हिरण्यगर्भ हैं। ये ही योगशास्त्रमें था। उस समय राजा करालजनकने उस आश्रमपर
- **Translation**: 

---

### Verse 11 (Bramha 0.8691)
- **Original**: महान्‌ और विरज्चि आदि नामोंसे प्रसिद्ध हैं तथा पहुँचकर वसिष्ठजीको हाथ जोड़कर प्रणाम किया
- **Translation**: 

---

### Verse 12 (Bramha 0.8692)
- **Original**: सांख्यशास्त्रमें भी उनका अनेकों नामोंसे वर्णन और विनययुक्त मधुरबाणीमें कहा--' भगवन्‌! जहाँसे
- **Translation**: 

---

### Verse 13 (Bramha 0.8693)
- **Original**: आता है। उनके नाना प्रकारके अनेक अद्भुत रूप ज्ञानी पुरुषोंको पुनः इस संसारमें नहीं आना
- **Translation**: 

---

### Verse 14 (Bramha 0.8694)
- **Original**: हैं। वे विश्वके आत्मा और एकाक्षर कहे गये हैं। पड़ता, उस सनातन ब्रह्मके स्वरूपका मैं वर्णन उन्होंने सम्पूर्ण त्रिलोकौकों स्वयं ही धारण कर सुनना चाहता हूँ। इसके सिवा जो क्षर कहा गया
- **Translation**: 

---

### Verse 15 (Bramha 0.8695)
- **Original**: रखा है तथा वे थहुत-से रूप धारण करनेके है, उसका तथा जिसमें इस जगत्‌का लय होता है,
- **Translation**: 

---

### Verse 16 (Bramha 0.8696)
- **Original**: कारण विश्वरूप नामसे प्रसिद्ध हैं। ये महातेजस्वी उस अनामय, कल्याणमय, अक्षरतत्वका भी ज्ञान
- **Translation**: 

---

### Verse 17 (Bramha 0.8697)
- **Original**: भगवान्‌ अपनों शक्तिसे महत्तत्वकी सृष्टि करके प्राप्त करना चाहता हूँ; अतः आप इस विषयका फिर अहंकार और उसके अभिमानी देवता प्रजापतिकाो उपदेश करें।' उत्पन्न करते हैं। राजस, तामस और सात्विक वसिष्ठजीने कहा--राजन्‌! सुनो। जिस प्रकार
- **Translation**: 

---

### Verse 18 (Bramha 0.8698)
- **Original**: भेदसे तोन प्रकारके अहंकारोंसे आकाश, वायु, इस जगतूका क्षरण (लय) होता है, उसको तथा
- **Translation**: 

---

### Verse 19 (Bramha 0.8699)
- **Original**: तेज, जल और पृथ्वी-ये पाँच महाभूत तथा जिसमें इसका लय होता है, उस अक्षरकों भी , शब्द, स्पर्श, रूप, रस और गन्ध--ये पाँच विषय बतलाता हूँ। देवताओंके बारह हजार वर्षोका एक
- **Translation**: 

---

### Verse 20 (Bramha 0.8700)
- **Original**: तथा कान, त्वचा, नेत्र, जिढ्ला और नासिका-ये
- **Translation**: 

---

