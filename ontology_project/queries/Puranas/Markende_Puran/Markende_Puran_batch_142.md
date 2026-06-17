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

### Verse 1 (Markende Puran 0.2821)
- **Original**: दूत उकच 4905 4 देंबि दैत्येश्षर: शुग्भस्वैलोक्ये परमेश्वर:। दूतो5हं प्रेषितस्तेत त्थत्सतकाशधिहागतः
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2822)
- **Original**: अव्याइताज़ः सर्वासु यः सदा देवयोनिषु। निर्जिताखिलदेैत्यारि: स यदाह श्रृणुष्व तत्‌
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2823)
- **Original**: 9, या0-इसके बाद बाही>कऋष्लीं 'शुम्भ उबाच' इतना आधिक प्राठ हैं। 2. पा0-तां च देवीं ततः।
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2824)
- **Original**: देखताआंद्वारा रा दत्नीका स्तुति 2092 35577 »/64 #$8 44:52 :0%%7-774 7 # # 4 8.&4:2522::00085:44: 84844 405::2::2.2.:0+ 566 +& 83 522.52.5.554 46 अजय मम जैलोक्यमशिलं मप्त देवा सशानुगा:। यज्जभागानई सर्वानुपाश्नामि पृथक्‌ पृथक # 908
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2825)
- **Original**: प्रैल्लोक्ये बररत्नानि मम वश्यान्यशेषतः। त्तथब गजरत्न॑ च क्षीगेदमथनोद्धुतमश्रर्त्न मप्तामरः । उच्च: अ्रवससंज़॑तत्प्रणिपत्य समर्पितम्‌
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2826)
- **Original**: यानि चान्यात्रि देवेषु गन्धर्वेदूरगेषु च। रत्रभूतानि भूतानि तानि मस्येव शोभने
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2827)
- **Original**: स्त्रीसस्‍त्रंभूतां त्वां देवि लोके मन्यामहे वयम्‌। सा त्वमस्मानुपागच्छ यतो रत्रभुजों बयम्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2828)
- **Original**: माँ बा मम्ानुज वापि निशुम्भमुरुधिक्रमम्‌
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2829)
- **Original**: हत्वा देवेन्द्रवाहनभ्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2830)
- **Original**: । भज त्व॑ चम्नलापाड़ि रत्नभूतासि लैं यत:
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2831)
- **Original**: परमैश्चर्यमतुल॑ प्राप्स्यसे मत्यरिग्रहात्‌। एलद खुद्धपा समालोच्य मत्परिग्रहततां तज
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2832)
- **Original**: दूत ओला--
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2833)
- **Original**: 105 # देवि ! दैत्यराज शुम्भ इस समय तीनों लोकोंके परमेश्वर हैं। मैं उन्होंका भेजा हुआ दूत हूँ और यहाँ तुम्हारे हरी पास आया हूँ
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2834)
- **Original**: उनको आज्ञा सद्रा सब देवता एक स्वससे महलते हैं। कोई उसका डार्बनद्नत नहीं कर सकता। बे सम्पूर्ण देववाओंकों परास्त कर चुके हैं। उन्होंने तुम्हो! लिये जो संदेश दिया है सुदो
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2835)
- **Original**: "सम्पूर्ण त्रिलोक़ों मेरे अधिकारपें है। देखता भी मेरी आज्ञाक अधीन चलते हैं। सम्पूर्ण बज्ञोंके भागोंकों में ही पृथकु-पृथक्‌ भोगठा हूँ
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2836)
- **Original**: तीनों लोकॉमें जितने श्रेष्ठ रज् हैं, वे सत्र मेरे अभधिकारमें हैं। देखराज इक बाहर ऐरावत्त. जो हाथियोंमें रक़के समान है. मैंने छोन लिया है
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2837)
- **Original**: क्षीस्सागरका पत्धन करनेसे जो अश्वग्ह उच्चे;क्षत। प्रकट जुआ था, उसे देबताओंते मेरे पैरोंपर पड़कर समर्पित किया है
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2838)
- **Original**: सुन्दरी ! ठाके सिवा और भी जितने रत्भुत पदार् देवताओं, गग्धर्वों और नामोंके पास
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2839)
- **Original**: बोलीं--
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2840)
- **Original**: 5. पा+--अलान्नि दत्णक। 2. घ2-हरन $ ञ्से
- **Translation**: 

---

