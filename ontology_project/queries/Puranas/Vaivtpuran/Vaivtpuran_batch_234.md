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

### Verse 1 (Vaivtpuran 13.10822)
- **Original**: इस सम्बन्धकों जोड़ा। विवाहकालमें महाराज राजा हैं। वे भगवान्‌ नारायणके अंशसे उत्पन्न
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10823)
- **Original**: भनन्दनने गजरत्ल, अश्वरल, अन्यान्य रल तथा हुए हैं और उत्तम गुणोंके भण्डार, सुन्दर,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10824)
- **Original**: मणियोंके आभूषण आदि बहुत दहेज दिये। सुविद्वान, सुस्थिर यौबनसे युक्त, योगी, पूर्वजन्मको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10825)
- **Original**: वृषभानु कलावतीको पाकर बड़ी प्रसन्नताके साथ बातोंको स्मरण करनेवाले और नवयुवक हैं।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10826)
- **Original**: निर्जन एवं स्मणीय स्थानमें उसके साथ विहार आपकी कन्या भी यज्ञकुण्डसे उत्पन्न हुई है; अत:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10827)
- **Original**: करने लगे। कलाबती एक पलका भी विरह अयोनिजा है। त्रिभुवनमोहिनी कन्या कलावती
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10828)
- **Original**: होनेपर स्वामीके बिना व्याकुल हों उठती थी भगवती कमलाकी अंश है और स्वभावत: शान्त
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10829)
- **Original**: और वृषभानु भी एक क्षणके लिये भी कलावतीके जान पड़ती है। वृषभानु आपकी पुत्रीके योग्य
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10830)
- **Original**: दूर होनेपर उसके बिना विकल हो जाते थे। हैं तथा आपकी पुत्री भी उन्हींके योग्य है।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10831)
- **Original**: वह राजकन्या पूर्वजन्मकी बातोंको याद रखनेवाली मुने! राजसभामें ऐसा कहकर नन्‍्दजी चुप
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10832)
- **Original**: देवी थी। मायासे मनुष्यरूपमें प्रकट हुई थी। हो गये। तब नृपश्रेष्ठ भनन्दनने विनयसे नम्न हो
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10833)
- **Original**: वृषभानु भी श्रीहरिके अंश और जातिस्मर थे उन्हें इस प्रकार उत्तर दिया। तथा कलावतीकों पाकर बड़े प्रसन्न थे। उन भ्रनन्दन बोले--ब्रजेश्वर! सम्बन्ध तो विधाताके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10834)
- **Original**: दोनोंका प्रेम प्रतिदिन नया-नया होकर बढ़ने वशकी बात है। वह मेरे द्वारा साध्य नहीं है।
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10835)
- **Original**: लगा। लीलावश पूर्वकालमें सुदामाके शाप और ब्रह्माजी ही सम्बन्ध करनेवाले हैं। मैं तो केवल
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10836)
- **Original**: श्रीकृष्फी आज्ञासे -श्रीकृष्णप्राणाधिका सती जन्मदाता हूँ। कौन किसकी पत्नी या कन्या है
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10837)
- **Original**: राधिका उन दोनोंकी अयोनिजा पुत्री हुईं। उसके तथा कौन किसका साधन-सम्पन्न पति है? इसे दर्शनमात्रसे वे दोनों दम्पति भवबन्धनसे मुक्त हो विधाताके सिवा और कौन जानता है? करमोंके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10838)
- **Original**: गये। नारद! इस प्रकार इतिहास कहा गया। अब अनुरूप फल देनेवाले विधाता ही सबके कारण
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10839)
- **Original**: जिसका प्रकरण चल रहा है, वह प्रसड़ सुनों। हैं। किया हुआ कर्म कभी निष्फल नहीं होता,
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10840)
- **Original**: उक़ इतिहास पापरूपी ईंधनकों जलानेके लिये उसका फल मिलकर ही रहेगा--ऐसा श्रुतिमें सुना
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10841)
- **Original**: प्रथलित अग्निकी शिखाके समान है।
- **Translation**: 

---

