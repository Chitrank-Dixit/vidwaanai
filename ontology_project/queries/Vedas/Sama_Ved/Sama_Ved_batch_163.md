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

### Verse 1 (Sama Ved 0.3241)
- **Original**: 1264. एप प्रत्नेन जन्मना देवो देवेभ्यः सुतः । हरि: पवित्रे अर्पति
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3242)
- **Original**: . यह दिव्य हरिताभ सोम, सदा से ही दैवीय गुणों की अभिवृद्धि करने में पवित्र होकर प्रयुक्त होता रहा है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3243)
- **Original**: 1265. एष 3 स्य पुरुक्षतो जज्ञानो जनयन्निष: । धारया पवते सुतः
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3244)
- **Original**: विशिष्ट कार्यक्षमता का जनक और पोषक-आहार उत्पन्न करने वाला यह सोम, अपने रस्त- प्रवाह से स्वाभाविकरूप से शुद्ध हो जाता है
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3245)
- **Original**: इति प्रथम: खण्ड:
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3246)
- **Original**: के के की
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3247)
- **Original**: द्वितीय: खण्ड:
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3248)
- **Original**: 1266. एप धिया यात्यण्व्या शूरो रथेभिराशुभि: । गच्छन्निद्धस्य निष्कृतम्‌
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3249)
- **Original**: अँगुलियों से निचोड़ा गया, शक्तिशाली यह सोम, तीव्र गतिशील रथ से विवेकपूर्वक इन्द्रदेव के निकट पहुँच जाता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3250)
- **Original**: 1267. एप पुरु धियायते बृहते देवतातये । यत्रामृतास आशत
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3251)
- **Original**: देवों से अधिष्ठितश्रेष्ठ यज्ञ स्थान में, यह सोम असंख्यों कर्म सम्पादन करने की अभिलाषा रखता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3252)
- **Original**: 1268. एत॑ मृजन्ति मर्ज्यमुप द्रोणेष्वायवः । प्रचक्राणं महीरिषः
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3253)
- **Original**: रसयुक्त (पोषक) अन्नों के उत्पत्तिकारक, शोधित होने योग्य सोमरस को क्ित्विग्गण संस्कारित करके कलशों में एकत्र करते हैं
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3254)
- **Original**: उत्तराचिके दश्षमो5 ध्याय: 10.3 1269. एष हितो वि नीयते3न्तः शुन्ध्यावता पथा । यदी तुझन्ति भूर्णय:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3255)
- **Original**: हविष्यान के रूप में प्रयुकत यह सोम वज्ञस्थल पर ले जाया जाता है, जहाँ से अध्वर्युगण उसे शुद्ध करते हुए देवताओं को समर्पित कर देते हैं
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3256)
- **Original**: 1270. एव रुक्मिभिरीयते वाजी शुभ्रेभिरंशुभिः । पति: सिन्धूनां भवन्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3257)
- **Original**: श्वेत रश्मियों से युक्त, रसों का अधिपति, प्रवहमान, शक्तिशाली सोम बेग से प्रवाहित होकर उपासकों के पास पहुँचता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3258)
- **Original**: 1279. एष श्रृड्राणि दोधुवच्छिशीते यूथ्यो3 वृषा । नृष्णा दधान ओजसा
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3259)
- **Original**: ऐश्वर्यवान्‌, यह सोम अपनी सामर्थ्य को उसी प्रकार प्रकट करता है, जिस प्रकार बलशाली वृषभ पशुओं के मध्य अपनी शक्ति को प्रकट करता है
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3260)
- **Original**: 1272. एप वसूनि पिब्दनः परुषा ययिवाँ अति । अब शादेघषु गच्छति
- **Translation**: 

---

