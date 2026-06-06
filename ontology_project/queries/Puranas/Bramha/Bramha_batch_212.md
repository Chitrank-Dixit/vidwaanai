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

### Verse 1 (Bramha 0.4221)
- **Original**: -ऋछणप्परूओई स्वामीसे कहा--'नाथ! मुझे ऐसा पुत्र दीजिये, जो
- **Translation**: 

---

### Verse 2 (Bramha 0.4222)
- **Original**: यदि निरन्तर इन नियमॉका पालन करती रहोगी अनेक गुणोंसे सम्पन्न, विश्वविजयी और जगद्ठन्द्य
- **Translation**: 

---

### Verse 3 (Bramha 0.4223)
- **Original**: तो तुम्हारा पुत्र ब्रिभुवनके ऐश्वर्यका भागी होगा।' हो तथा जिसके जन्म लेनसे मैं संसारमें वीरजननी
- **Translation**: 

---

### Verse 4 (Bramha 0.4224)
- **Original**: दितिने स्वामीके समक्ष प्रतिज्ञा की-'मैं इन कहला सकूँ।” कश्यपजीने कहा--' देवि! मैं तुम्हें
- **Translation**: 

---

### Verse 5 (Bramha 0.4225)
- **Original**: नियमोंक्र ठीक-ठीक पालन करूँगी।' फिर कश्यपजी एक श्रेष्ठ व्रतका उपदेश करता हूँ, जो बारह
- **Translation**: 

---

### Verse 6 (Bramha 0.4226)
- **Original**: देवताओंकि यहाँ चले गये। इधर दितिका पुण्यजनित वर्षोतक पालन करनेके बाद फल देता है। उसके
- **Translation**: 

---

### Verse 7 (Bramha 0.4227)
- **Original**: बलवान्‌ गर्भ दिनोँदिन बढ़ने लगा। इन सब बाद आकर तुम्हारे मनके अनुकूल गर्भका आधान
- **Translation**: 

---

### Verse 8 (Bramha 0.4228)
- **Original**: बातोंको मय नामक दैत्य अपनी मायाके बलसे करूँगा, क्योंकि ब्रत आदिके द्वारा निष्पाप हो
- **Translation**: 

---

### Verse 9 (Bramha 0.4229)
- **Original**: जानता था। उसकी इन्द्रसे मित्रता थी। दोनोंमें जानेपर ही सम्पूर्ण मनोरथ सिद्ध होते हैं।' बड़ा प्रेम था। उसने इन्द्रके पास एकान्तमें जाकर पतिका यह वचन सुत्॒कर दितिकों बड़ी
- **Translation**: 

---

### Verse 10 (Bramha 0.4230)
- **Original**: विनयपूर्वक कहा-'दिति और दनुने विशेष प्रसन्नता हुईं। उसने कश्यपजीको नमस्कार करके
- **Translation**: 

---

### Verse 11 (Bramha 0.4231)
- **Original**: अभिप्रायसे कश्यपजीको संतुष्ट किया है। दितिका उनके बताये हुए ब्रतका विधिपूर्वक पालन
- **Translation**: 

---

### Verse 12 (Bramha 0.4232)
- **Original**: गर्भ दिनोंदिन बढ़ता है, उसमें नाना प्रकारकी किया। जो लोग तीर्थोंकी सेवा, सुपात्रोंकों दान
- **Translation**: 

---

### Verse 13 (Bramha 0.4233)
- **Original**: शक्तियाँ हैं।' तथा व्रतका पालन आदि नहीं करते, वे अपनी
- **Translation**: 

---

### Verse 14 (Bramha 0.4234)
- **Original**: . भारदजीने पूछा--देवेश्वर! महाबली मय नामक अभीष्ट वस्तुओंको कैसे प्राप्त कर सकते हैं।! दैत्य तो नमुचिका प्रिय भ्राता है और नमुचि दितिका ब्रत पूरा होनेपर कश्यपजीने गर्भाधान
- **Translation**: 

---

### Verse 15 (Bramha 0.4235)
- **Original**: इन्द्रके हाथसे मारा गया था। फिर उसकी अपने किया और एकान्तमें अपनी प्रिय पत्नी दितिसे
- **Translation**: 

---

### Verse 16 (Bramha 0.4236)
- **Original**: भाईके शत्रुसे मित्रता कैसे हुई? कहा--'शुचिस्मिते! तपस्वी मुनि भी विहित! ब्रह्माजी बोले--पूर्वकालमें नमुचि दैत्योंका कर्मकी अबहेलना करनेसे मनोवाज्छित पदार्थ
- **Translation**: 

---

### Verse 17 (Bramha 0.4237)
- **Original**: राजा था, उसका इन्द्रके साथ बड़ा भयंकर बैर नहीं पा सकते। अतः तुम्हें कोई निन्दित कर्म
- **Translation**: 

---

### Verse 18 (Bramha 0.4238)
- **Original**: हुआ। एक समयकी बात है-इन्द्र युद्ध छोड़कर नहीं करना चाहिये। दोनों संध्याओंके समय
- **Translation**: 

---

### Verse 19 (Bramha 0.4239)
- **Original**: कहीं जा रहे थे। यह देखकर दैत्यराज नमुचि भी सोना, कहाँ जाना अथवा बाल खोले रहना
- **Translation**: 

---

### Verse 20 (Bramha 0.4240)
- **Original**: उनके पीछे लग गया। उसे आगे देख इन्द्र भयसे निषिद्ध है। संध्याकाल भूतोंसे व्याप्त रहता है।
- **Translation**: 

---

