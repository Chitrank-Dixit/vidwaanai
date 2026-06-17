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

### Verse 1 (Shiv Puran 0.2801)
- **Original**: आप अडछुत हैं, आपकी जब हो । आप अक्षुद्र (महान) हैं, आपकी जय हो । आप अक्षत (निर्विकार) हैं, आपकी जय हो। आधार हैं तथा ्ञाच्तिपय मज़लू्के निकेतन अजन्पा शिव ! आपकी जय हो । निर्सह्त हैं। आपकी जय हो
- **Translation**: 

---

### Verse 2 (Shiv Puran 0.2802)
- **Original**: झंकर ! आपकी जय हो
- **Translation**: 

---

### Verse 3 (Shiv Puran 0.2803)
- **Original**: है 4 #-&+-4-5 3.44 3. 4.& 30%. %5%-3 6 %03#730/ 48-28 2.44 24322 48 8 8 2.8 2/ 7 0//4/4/// 6 थे जी ची महाभुजअ॒ महासार महागुण मसहाकथ। महाबल गहागाय पटारस म्रहात्व
- **Translation**: 

---

### Verse 4 (Shiv Puran 0.2804)
- **Original**: 9 8 महाबाहो ! महासार ! महागुण ! महतो कीर्तिकथासे युक्त ! महाबली ! अहामायाती ! महान्‌ रसिक तथा महारथ ! आपकी जय हो
- **Translation**: 

---

### Verse 5 (Shiv Puran 0.2805)
- **Original**: नमः परमदेवाव नमः परमहेतले। नपः दिवाय झ्ञाक्ताय नमः दिवतराय ते
- **Translation**: 

---

### Verse 6 (Shiv Puran 0.2806)
- **Original**: आप परम आराध्यको नमस्कार है। आप परम क्कारणकों नमस्कार है। झञान्त शिवकों नमस्कार हैं और आप परम कर्याणामय प्रभुको नमस्कार है
- **Translation**: 

---

### Verse 7 (Shiv Puran 0.2807)
- **Original**: ल्वदघीनगिर्द कृत्खे जगद्धि सहुरालुस्म
- **Translation**: 

---

### Verse 8 (Shiv Puran 0.2808)
- **Original**: अतस्त्यद्विदितामाजं क्षमते को्यतियर्तितुम्‌
- **Translation**: 

---

### Verse 9 (Shiv Puran 0.2809)
- **Original**: देवताओं और असुरोंसहित यह सम्पूर्ण जगत्‌ आपके अथीन है। अत: आपकी आज्ञाका उल्त्वक्डन करनेमें कौन समर्थ हो सकता है
- **Translation**: 

---

### Verse 10 (Shiv Puran 0.2810)
- **Original**: । जवानतोज्नुग्क्वास्मै प्रार्थितं सम्प्रयच्चाणु
- **Translation**: 

---

### Verse 11 (Shiv Puran 0.2811)
- **Original**: है सनातनदेव ! यह सेवक एकमात्र आपके ही आश्रित है; अत: आप इसपर अनुप्रह करके इसे इसकी श्र्थित वस्तु अदान करें
- **Translation**: 

---

### Verse 12 (Shiv Puran 0.2812)
- **Original**: जयाम्क्कि जगचातर्जय सर्वजगनधि। जयारवध्रिकैशवयें जयातुपमतिप्रहे । (4
- **Translation**: 

---

### Verse 13 (Shiv Puran 0.2813)
- **Original**: अम्बिके ! जगन्मात: ! आपकी जय हो। सर्वजगन्ययी ! आपकी जय हो। असीम ऐश्वर्यशाल्ननि ! आपकी जय हो । आपके श्रीतिग्रहकी कहीं उपमा नहीं है, आपकी जय हो
- **Translation**: 

---

### Verse 14 (Shiv Puran 0.2814)
- **Original**: जय वाहुमनसातीते जवाबिदध्यात्तभाज़िके। जय जच्यजराहीने जय कालोक्षणेत्तो
- **Translation**: 

---

### Verse 15 (Shiv Puran 0.2815)
- **Original**: मन, जाणीसे अतीत झिखे ! आपकी जय हो। अक्षानाधकारका भक्षन करनेवाली देधि ! आपकी जय हो
- **Translation**: 

---

### Verse 16 (Shiv Puran 0.2816)
- **Original**: जन्म और जरासे रहित उमे ! आपकी जय हो । कालसे भी अतिदाद्र उत्कृष्ट शाक्तिबात्ठी दुगें ! आपको जय हो
- **Translation**: 

---

### Verse 17 (Shiv Puran 0.2817)
- **Original**: अयानेकायेघानस्थे जय विश्वेशवरप्रिये। जय किधसुयाताध्ये जय विश्वजिजुम्मिणि
- **Translation**: 

---

### Verse 18 (Shiv Puran 0.2818)
- **Original**: अनेक प्रकारके विधानोंसमें. स्थित परमेश्वरि ! आपकी जय हो। विध्वनाथ- प्रिये! आपकी जय हो। समस्त देवताओंकी आराधनीया देवि ! आपकी जब हो । सम्पूर्ण विश्वका विस्तार करनेवाली जगदम्बिके ! आपकी जय हो
- **Translation**: 

---

### Verse 19 (Shiv Puran 0.2819)
- **Original**: जय मड्डस्दित्याड्ि जय मज्जल्प्दीपिके। जय मदुलचारित्रे जय मज़लदायिनि
- **Translation**: 

---

### Verse 20 (Shiv Puran 0.2820)
- **Original**: मड्ल्पय दिव्य अद्रोंबाली देवि ! आपकी जय हो। मज़ूल्कको प्रकादित करनेवाली ! आपकी जय हो। चरिज्रवाली सर्वमज्ले ! आपकी जय हो । मक्वलूदायिनि ! आपकी जय हो
- **Translation**: 

---

