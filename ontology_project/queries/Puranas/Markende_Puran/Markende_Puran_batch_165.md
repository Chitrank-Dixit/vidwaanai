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

### Verse 1 (Markende Puran 0.3281)
- **Original**: 'दुए दुर्गे! तू बलके अभिमानमें आकर झूठ-मूठका श्रंपंड न दिखा। तू बड़ी मानिनों जर्गीं हुई है, किन्तु दूसरी रिथ्रियोंके यलका सहारा लेकर हड़ती है '
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3282)
- **Original**: ब्ैन्युपाच
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3283)
- **Original**: / एकेयाह जगत्यत्न द्वितीयां क्ॉ मपापरा।
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3284)
- **Original**: यश्यैता दुष्ट मस्येव बिशन्त्यों मद्दिभूतय: 5 मन
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3285)
- **Original**: देखो ओोलीं--
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3286)
- **Original**: ओ दुएफ ! पं अकेली हो हूँ। इस संस्रारपें मेरे स्िच्मा दूसरा कौने है। देख, 2. पाजनपदु0 2. इसके खाद किलों-किसी प्रत्तियें 'कषिर्षाथ' हतना आंधिक पाठ है। . देवीके शगेरपें लीन हो गवीं। उस समय केवल अम्निका देवी ही रह गयों
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3287)
- **Original**: देव्ुकाच
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3288)
- **Original**: अई विभूत्या श्रहुभिरिह रूप्यदास्थिता। तत्संइतं मयैकैच तिष्ठाम्याजौं स्थिरों भव॑ं
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3289)
- **Original**: देवी ओलीं-- 4 7
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3290)
- **Original**: में अपनों ऐश्वर्शशक्तिसे अगेक रुपरोंमें बहाँ उपस्थित हुई थों। उन सब रूपोंकों मैंने समेट लिया। अब अकेत्ती हो युद्धमें खड़ो हूँ। तुम भी स्थिर हो जाओ
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3291)
- **Original**: 228 * संक्षिप्त पार्कण्डेयपुराण * ऋषिरुताच
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3292)
- **Original**: ततः प्रववृते युद्ध॑ देव्या: शुम्भस्य चोभयो:। पश्यतां सर्वदेवानामसुराणां च दारुणम्‌ृग10
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3293)
- **Original**: शरवर्ष: शितै: शस्त्रैस्तथास्त्रैत्ैव दारुणै: तबोर्युद्धमभूद्धूय:... सर्वलोकभयड्भूरम्‌
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3294)
- **Original**: दिव्यान्यस्त्राणि शतशो मुमुच्चे यान्यथाम्बिका। बभञ्ञ॒ तानि दैत्येन्नस्तत्प्रतीघातकर्तृभि:
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3295)
- **Original**: मुक्तानि तेन चास्व्राणि दिव्यानि परमेश्चरी। बभझ्ञ लीलयैबोग्रहुद्जारोच्यारणादिभि:
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3296)
- **Original**: ततः शरशरतैर्देबरीमाच्छादयत सो5सुरः। सापि तत्कुपिता देवी धनुश्चिच्छेद चेषुभि:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3297)
- **Original**: छिन्ने थनुषि दैत्वेन्द्रस्त्था शक्तिमधाददे। चिच्छेद देवी चक्रेण तामप्यस्य करे स्थिताम्‌
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3298)
- **Original**: ततः खड़्गमुपादाय शतचन्द्रं च भानुमत्‌। अभ्यधावत्तदार देवीं दैत्यानामधिपेश्वर:
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3299)
- **Original**: तस्यापतत एबाशु खड्ग॑ चिच्छेद चण्डिका। धनुर्मुक्तै: शितैर्बाणैश्वर्म चार्ककरामलम्‌
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3300)
- **Original**: हताश्चः स तदा दैत्यश्छिन्नधन्वा विसारथि:। जग्राह मुद्रं घोरमम्बिकानिधनोहात:
- **Translation**: 

---

