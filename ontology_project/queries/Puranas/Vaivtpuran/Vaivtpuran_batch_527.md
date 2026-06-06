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

### Verse 1 (Vaivtpuran 32.7677)
- **Original**: देखा है। सुन्दरि! पादुका, चमड़ेकी रस्सियोंकी पटापट गिर रहे थे। यह भी देखा कि मेरे हाथसे [बहुत बड़ी राशि और कुम्हारके चाकको भूमिपर भरा हुआ कलश गिर पड़ा और चकनाचूर हो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 32.7678)
- **Original**: घूमते हुए देखा। सुव्रते! रातमें देखा कि आँधीने गया तथा आकाशसे चन्द्रमण्डल गिर रहा है।
- **Translation**: 

---

### Verse 3 (Vaivtpuran 32.7679)
- **Original**: एक सूखे पेड़को झकझोरकर उखाड़ दिया है पुनः आकाशसे भूतलपर गिरते हुए सूर्यमण्डलको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 32.7680)
- **Original**: और वह वृक्ष पुनः उठकर खड़ा हो गया है तथा उल्कापात, धूमकेतु और सूर्य एवं चन्द्रमाके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 32.7681)
- **Original**: तथा बिना सिर्का धड़ चक्कर काट रहा है। श्रेष्टे ग्रहणको देखा। फिर एक ऐसे भयानक पुरुषकों एक गुँथी हुई मुण्डोंकी माला, जिसमें अत्यन्त सामनेसे आते हुए देखा, जिसका आकार बेडौल
- **Translation**: 

---

### Verse 6 (Vaivtpuran 32.7682)
- **Original**: भयंकर दाँत दीख रहे थे तथा जिसे आँधीने था, मुख विकराल था और जिसके शरीरपर वस्त्र
- **Translation**: 

---

### Verse 7 (Vaivtpuran 32.7683)
- **Original**: चूर-चूर कर दिया था, मुझे दीख पड़ी। रातमें नहीं था। रातमें मैंने यह भी देखा कि एक बारह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 32.7684)
- **Original**: मैंने यह भी देखा कि झुंड-के-झुंड भूत-प्रेत, वर्षकी अवस्थावाली युवती, जो वस्त्र और
- **Translation**: 

---

### Verse 9 (Vaivtpuran 32.7685)
- **Original**: जिनके बाल खुले हुए थे और जो मुखसे आग आभूषणोंसे सुशोभित थी, रुष्ट होकर मेरे घरसे
- **Translation**: 

---

### Verse 10 (Vaivtpuran 32.7686)
- **Original**: उगल रहे थे-मुझे लगातार भयभीत कर रहे बाहर जा रही है। (जाते समय उसने कहा--)
- **Translation**: 

---

### Verse 11 (Vaivtpuran 32.7687)
- **Original**: हैं। रातमें मैंने जला हुआ जीब, झुलसा हुआ “राजेन्र! आप शोकपूर्ण चित्तसे बोलते हैं; अतः
- **Translation**: 

---

### Verse 12 (Vaivtpuran 32.7688)
- **Original**: वृक्ष, व्याधिग्रस्त मनुष्य और अद्भहीन शूद्रको मैं आपके घरसे वनको चली जाऊँगी; इसके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 32.7689)
- **Original**: भी देखा है। रातमें मैंने यह भी देखा कि सहसा लिये मुझे आज्ञा दीजिये।' मैंने देखा कि क्रुद्ध
- **Translation**: 

---

### Verse 14 (Vaivtpuran 32.7690)
- **Original**: घर, पर्वत और वृक्ष गिर रहे हैं तथा बारंबार ब्राह्मण, संन्‍्यासी और गुरु मुझे शाप दे रहे हैं
- **Translation**: 

---

### Verse 15 (Vaivtpuran 32.7691)
- **Original**: वज्पात हो रहा है। रातमें घर-घरमें कुत्ते और और दीवालपर चित्रित पुत्तलिकाएँ नाच रही हैं।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 32.7692)
- **Original**: सियार निश्चितरूपसे बारंबार रो रहे थे, मुझे यह रातमें मैंने देखा कि चञ्लल गीधों, कौओं और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 32.7693)
- **Original**: भी दिखायी पड़ा है। मैंने एक पुरुषको देखा-जो भैंसोंका समूह मुझे पीड़ा पहुँचा रहा है।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 32.7694)
- **Original**: दिगम्बर था, जिसके बाल बिखरे थे और जो महारानी ! मैंने तेल, तेलौद्वारा घुमाया जाता हुआ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 32.7695)
- **Original**: नीचे मस्तक तथा पैर ऊपर करके पृथ्वीपर घूष कोल्हू और पाशधारी दिगम्बरोंकों देखा। मैंने
- **Translation**: 

---

### Verse 20 (Vaivtpuran 32.7696)
- **Original**: रहा था। उसकी आकृति और बोली विकृत थी। रातमें देखा कि मेरे घरमें परमानन्ददायक
- **Translation**: 

---

