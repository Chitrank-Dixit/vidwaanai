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

### Verse 1 (Bramha 0.4701)
- **Original**: वो उनपर बड़े-बड़े शस्त्रोंकी मार पड़ने लगी। नन्दनवनकी याद आती है।' यों कहकर महात्मा
- **Translation**: 

---

### Verse 2 (Bramha 0.4702)
- **Original**: इससे भवभीत होकर आत्रेयने कहा--“मैं इन्द्र आत्रियने तपस्याके प्रभावसे विश्वकर्माको बुलाया और
- **Translation**: 

---

### Verse 3 (Bramha 0.4703)
- **Original**: नहीं हूँ। मेरी यह भार्या भी शची नहीं है।न तो इस प्रकार कहा--'महात्मन्‌! मैं इन्द्रका पद चाहता [यह इन्द्रपुरी है और न यहाँ इन्द्रका नन्दनवन है। हूँ। आप शीघ्र ही यहाँ इद्रपुरौका निर्माण कौजिये।
- **Translation**: 

---

### Verse 4 (Bramha 0.4704)
- **Original**: वृत्रहन्ता, वज़धारी और सहस्त्र नेत्रोंवाले इन्द्र दो इसके विपरीत यदि आपने कोई बात मुँहसे निकाली
- **Translation**: 

---

### Verse 5 (Bramha 0.4705)
- **Original**: स्वर्गमें हो हैं। मैं तो चेदबेत्ता ब्राह्मण हूँ. और तो मैं निशय ही आपको भस्म कर डालूँगा।'
- **Translation**: 

---

### Verse 6 (Bramha 0.4706)
- **Original**: ब्राह्मणोंके साथ ही गौतमीके तटपर निवास करता आत्रेयके यों कहनेपर प्रजापति विश्वकमनि
- **Translation**: 

---

### Verse 7 (Bramha 0.4707)
- **Original**: हूँ। दुर्देवकी प्रेरणासे मैंने यह कर्म कर डाला, जो तत्काल हो वहाँ मेरुपर्वत, देवपुरी, कल्पवृक्ष, [व तो वर्तमान कालमें सुख देनेवाला है और न कल्पलता, कामधेनु, बच्र आदि मणियोंसे विभूषित,
- **Translation**: 

---

### Verse 8 (Bramha 0.4708)
- **Original**: भविष्यमें ही।' सुन्दर तथा अत्यन्त चित्रकारी किये हुए गृह । असुर बोले--मुनिश्रेष्ठ आत्रेय! यह इन्द्रका बनाये। इतना ही नहीं, उन्होंने सर्वाद्भसुन्दरी
- **Translation**: 

---

### Verse 9 (Bramha 0.4709)
- **Original**: अनुकरण छोड़कर यहाँका सारा वैभव समेट लो, शचीकी भी आकृति बनायी, जो कामदेवकी
- **Translation**: 

---

### Verse 10 (Bramha 0.4710)
- **Original**: तभो तुम कुशलसे रह सकते हो; अन्यथा नहीं। विहारशाला-सी प्रतीत होती थी। क्षणभरमें सुधर्मा
- **Translation**: 

---

### Verse 11 (Bramha 0.4711)
- **Original**: . तब आत्रेयने कहा--' मैं अग्रिको शपथ खाकर सभा, मनोहारिणी अप्सराएँ, उच्चै:श्रवा अश्च,
- **Translation**: 

---

### Verse 12 (Bramha 0.4712)
- **Original**: सच-सच कहता हूँ--आपलोग जैसा कहेंगे, वैसा ऐरावत हाथी, वज़ आदि अस्त्र और सम्पूर्ण
- **Translation**: 

---

### Verse 13 (Bramha 0.4713)
- **Original**: ही करूँगा।' दैत्योंसे यों कहकर वे पुन: विश्वकर्मासे देवताओंका निर्माण हो गया। अपनी पत्नीके मना
- **Translation**: 

---

### Verse 14 (Bramha 0.4714)
- **Original**: बोले--' प्रजापते! आपने मेरी प्रसन्नताके लिये जो करनेपर भी आत्रेयने शचीके समान रूपबाली उस
- **Translation**: 

---

### Verse 15 (Bramha 0.4715)
- **Original**: इन्द्रपदका निर्माण किया था, इसका फिर उपसंहार स्त्रीकों अपनी भार्या बना लिया। बद्च आदि , कर लीजिये और ऐसा करके मुझ ब्राह्मण मुनिकी आदि सब कुछ यहाँ उसी तरहसे होने लगा, जिस
- **Translation**: 

---

### Verse 16 (Bramha 0.4716)
- **Original**: 65,517: कु प्रकार वह इन्द्रपुरमें देखा गया था। स्वर्गलोकका
- **Translation**: 

---

### Verse 17 (Bramha 0.4717)
- **Original**: # 4 सम्पूर्ण सुख पाकर मुनिवर आत्रेयका चित बहुत
- **Translation**: 

---

### Verse 18 (Bramha 0.4718)
- **Original**: प्रसन्न हुआ। आपातरमणीय विषयोंकी भी भला,
- **Translation**: 

---

### Verse 19 (Bramha 0.4719)
- **Original**: 0 किस पुरुषको अपेक्षा नहीं होती। दैत्यों और दानवोंने जब स्वर्गका वैभव पृथ्वोपर उतरा हुआ सुना, तब उन्हें बड़ा क्रोध हुआ। वे परस्पर कहने लगे-'क्या कारण है कि इन्द्र स्वर्गलोककों
- **Translation**: 

---

### Verse 20 (Bramha 0.4720)
- **Original**: छोड़कर पृथ्वीपर सुख भोगनेके लिये आया है?
- **Translation**: 

---

