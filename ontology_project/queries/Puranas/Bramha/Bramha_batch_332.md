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

### Verse 1 (Bramha 0.6621)
- **Original**: आप श्वेत, दीर्घ आदि सम्पूर्ण कल्पनाओंसे रहित अदितिको कुण्डल देनेके लिये स्वर्गलोकमें गये।
- **Translation**: 

---

### Verse 2 (Bramha 0.6622)
- **Original**: हैं, जन्म आदि विकारोंसे पृथक्‌ हैं तथा स्वप्न आदि तीनों अवस्थाओंसे परे हैं; आपको नमस्कार है। अच्युत! सन्ध्या, रात्रि, दिन, भूमि, आकाश,
- **Translation**: 

---

### Verse 3 (Bramha 0.6623)
- **Original**: आप ही हैं। ईश्वर! आप न्रह्मा, विष्णु और शिव
- **Translation**: 

---

### Verse 4 (Bramha 0.6624)
- **Original**: नामक अपनी मूर्तियोंसे जगत्‌की सृष्टि, स्थिति और संहार करनेवाले हैं
- **Translation**: 

---

### Verse 5 (Bramha 0.6625)
- **Original**: आप कर्ताओंके भी अधिपति हैं। यह चराचर जगत्‌ आपकी मायाओंसे व्याप्त है। जनार्दन! अनात्म वस्तुमें जो आत्मबुद्धि होती है, वह आपकी माया है। उसीके द्वारा अहंता और ममताका भाव उत्पन्न होता है। नाथ! इस संसारमें जो कुछ होता है, वह सब आपकी मायाकी ही चेष्टा है। भगवन्‌! जो मनुष्य अपने धर्ममें तत्पर 47 5
- **Translation**: 

---

### Verse 6 (Bramha 0.6626)
- **Original**: , श्ष हो आपकी निरन्तर आराधना करते हैं, वे अपनी 7 2 8/ का 4 # 8
- **Translation**: 

---

### Verse 7 (Bramha 0.6627)
- **Original**: मुक्तिके लिये इस सारी मायाको तर जाते हैं। ब्रह्मा 05 ी (8
- **Translation**: 

---

### Verse 8 (Bramha 0.6628)
- **Original**: आदि सम्पूर्ण देवता, मनुष्य और पशु--ये सभी वरुणके छत्र, मणिपर्वत और प्लीसहित श्रीकृष्णको
- **Translation**: 

---

### Verse 9 (Bramha 0.6629)
- **Original**: श्रीविष्णुमायाके महान्‌ भँवरमें पड़े हुए मोहान्धकारसे पीठपर लिये गरुड़जी मौजसे चले जा रहे थे
- **Translation**: 

---

### Verse 10 (Bramha 0.6630)
- **Original**: स्वर्गके
- **Translation**: 

---

### Verse 11 (Bramha 0.6631)
- **Original**: आवृत हैं। भगवन्‌! जो आपकी आराधना करके द्वारपर पहुँचकर श्रीकृष्णने शद्लु बजाया। शद्डुकी
- **Translation**: 

---

### Verse 12 (Bramha 0.6632)
- **Original**: भोगोंको प्राप्त करना चाहते हैं, वे आपकी मायाद्वारा आवाज सुनकर सम्पूर्ण देवता आर्घ्यपात्र लिये
- **Translation**: 

---

### Verse 13 (Bramha 0.6633)
- **Original**: बँधे हुए हैं। मैंने भी पुत्रकी कामनासे और भगवान्‌की सेवामें उपस्थित हुए। उनके द्वारा पूजित
- **Translation**: 

---

### Verse 14 (Bramha 0.6634)
- **Original**: शत्रुपक्षका नाश करनेके लिये आपकी आराधना हो भगवान्‌ श्रीकृष्ण देवमाता अदितिके महलमें गये।
- **Translation**: 

---

### Verse 15 (Bramha 0.6635)
- **Original**: की है, मोक्षके लिये नहीं। यह आपकी मायाका वह भव्य भवन श्वेत बादलोंके समान धवल और
- **Translation**: 

---

### Verse 16 (Bramha 0.6636)
- **Original**: ही विलास है। पुण्यरहित मनुष्य यदि कल्पवृक्षसे पर्वत-शिखरके सदृश ऊँचा था। उसमें प्रवेश करके
- **Translation**: 

---

### Verse 17 (Bramha 0.6637)
- **Original**: भी कौपीनमात्र ही लेनेकी इच्छा करे तो यह भगवान्‌ने अदितिको देखा और इद्धसहित उनके
- **Translation**: 

---

### Verse 18 (Bramha 0.6638)
- **Original**: अपराध उसके अपने ही पापकर्मोंका है। अपनी
- **Translation**: 

---

### Verse 19 (Bramha 0.6639)
- **Original**: + श्रीकृष्णकी संततिं, अनिरुद्धके विवाहमें रुक्मीका दध तथा इख्धकी पराजय * मायासे सम्पूर्ण जगत॒को मोहित करनेवाले अविनाशी
- **Translation**: 

---

### Verse 20 (Bramha 0.6640)
- **Original**: परिजातकों गरुड़्पर रख लिया। यह देख उस परमेश्वर! मुझपर प्रसन्न होइये। ज्ञानस्वरूप सम्पूर्ण
- **Translation**: 

---

