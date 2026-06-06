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

### Verse 1 (Bramha 0.5241)
- **Original**: (170 । 45-46)
- **Translation**: 

---

### Verse 2 (Bramha 0.5242)
- **Original**: स्षड « संक्षिप्त ब्रह्मपुराण + उस समय गौतमीके दक्षिण-तटपर भगवान्‌ योगेश्वस्के
- **Translation**: 

---

### Verse 3 (Bramha 0.5243)
- **Original**: किया और योगेश्वर भगवान्‌ विष्णुकी विधिपूर्वक सामने ब्राह्मणने वैश्वको गिरा दिया और उसकी
- **Translation**: 

---

### Verse 4 (Bramha 0.5244)
- **Original**: पूजा की। विभीषणका पुत्र भी दूसरे विभीषणके आँखें निकाल लीं। फिर कहा--'वैश्य ! प्रतिदिन
- **Translation**: 

---

### Verse 5 (Bramha 0.5245)
- **Original**: ही समान धर्मात्मा था। उसे लोग बैभीषणि कहते धर्मकी प्रशंसा करनेसे ही तुम इस दशाको पहुँचे
- **Translation**: 

---

### Verse 6 (Bramha 0.5246)
- **Original**: थे। वैभीषणिने वैश्यको देखा और उससे वार्तालाप हो। तुम्हारा धन गया, आँखें गयीं और दोनों हाथ
- **Translation**: 

---

### Verse 7 (Bramha 0.5247)
- **Original**: किया। वैश्यका यथावत्‌ वृत्तान्त जानकर उस काट लिये गये। मित्र! अब तुमसे बिदा लेकर
- **Translation**: 

---

### Verse 8 (Bramha 0.5248)
- **Original**: धर्मज्ञने अपने पिता लझ्भापति महात्मा विभीषणको जाता हूँ। फिर कभी बातचीतमें इस तरह धर्मकी
- **Translation**: 

---

### Verse 9 (Bramha 0.5249)
- **Original**: बतलाया। लड्ढेश्वनने अपने गुणाकर पुत्रसे प्रशंसा न करना।' यों कहकर गौतम चला गया।
- **Translation**: 

---

### Verse 10 (Bramha 0.5250)
- **Original**: प्रसन्नतापूर्वक कहा--'बेटा! भगवान्‌ श्रीराम मेरे उसके जानेपर वैश्यप्रवर मणिकुण्डल धन, याहु
- **Translation**: 

---

### Verse 11 (Bramha 0.5251)
- **Original**: गुरु-आराध्यदेव हैं और उनके आदरणीय भक्त और नेत्रसे रहित होनेके कारण शोकग्रस्त हो
- **Translation**: 

---

### Verse 12 (Bramha 0.5252)
- **Original**: हनुमानजी मेरे सखा हैं। आजसे बहुत पहले एक गया। तथापि वह निरन्तर धर्मका ही स्मरण करता
- **Translation**: 

---

### Verse 13 (Bramha 0.5253)
- **Original**: कार्य आ पड़नेपर हनुमानजी बहुत बड़ा पर्वत था। अनेक प्रकारकी चिन्ता करते हुए वह
- **Translation**: 

---

### Verse 14 (Bramha 0.5254)
- **Original**: उठा लाये थे, जो सब प्रकारकी ओषधियोंका भूतलपर निश्वेष्ट होकर पड़ा था। उसके हृदयमें
- **Translation**: 

---

### Verse 15 (Bramha 0.5255)
- **Original**: भण्डार था।उस समय दो ओषधियोंकी आवश्यकता उत्साह नहीं रह गया था। बह शोक-सागरमें डूबा
- **Translation**: 

---

### Verse 16 (Bramha 0.5256)
- **Original**: थी--विशल्यकरणी और मृतसंजीबनी। उन दोनों हुआ था। दिन बीता, रजनीका आगमन हुआ और
- **Translation**: 

---

### Verse 17 (Bramha 0.5257)
- **Original**: ओषधियोंको लाकर उन्होंने भगवान्‌ श्रीरामको चअन्द्रमण्डलका उदय हो गया। उस दिन शुक्ल
- **Translation**: 

---

### Verse 18 (Bramha 0.5258)
- **Original**: अर्पित किया। जब उनको आवश्यकता पूर्ण हो पक्षकी एकादशी थी। एकादशीको वहाँ लड्ढासे
- **Translation**: 

---

### Verse 19 (Bramha 0.5259)
- **Original**: गयी, तब बे पुन: उस पर्वतको उठाकर हिमालयपर विभीषण आया करते थे। उस दिन भी आये;
- **Translation**: 

---

### Verse 20 (Bramha 0.5260)
- **Original**: ले गये और बहीं रख आये। हनुमानजी बड़े उन्होंने पुत्र और राक्षसोंसहित गौतमी गज्जामें स्नान
- **Translation**: 

---

