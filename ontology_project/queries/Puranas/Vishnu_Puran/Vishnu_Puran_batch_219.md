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

### Verse 1 (Vishnu Puran 0.4361)
- **Original**: हे द्विज ! मैं तो पहले ही महाभाग कपिलमुनिसे यह प्रष्मभभ्युद्यतो गत्वा श्रेयः कि त्वत्र शंस मे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4362)
- **Original**: पछनेके लि कि बताइये *संसारमें मनुष्योंका श्रेय किसमें तदन्तरे सच भवता यदेतद्वाक्यमीरितम्‌। तेनैब परमार्थार्थ त्वयि चेत: प्रधावति
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4363)
- **Original**: कपिलर्षिर्भगवत: सर्वभूतस्य वै द्विज
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4364)
- **Original**: विष्णोरंश्ो जगन्योहनाशायोवीमुपागतः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4365)
- **Original**: 9 स॒ एवं भगवाहब्ूनमस्मा्क हितकाम्यया। च्रत्यक्षतामत्र गतो यथैतझ्धबतोच्यते
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4366)
- **Original**: 90 तन्यह्वां प्रणताय त्वं यच्छेय: परम द्विज । तद्ददाखिलविज्ञानजलवीच्युदधिर्भवानू_
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4367)
- **Original**: 11 ऑकाण उबाच भूप पृच्छसि कि श्रेय: परमार्थ नु पृष्छसि । श्रेयांस्यपरमार्थानि अशेषाणि च॒ भूपते
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4368)
- **Original**: 12 देवताराधन॑ कृत्वा धनसम्पदमिच्छति । पुत्रानिच्छति राज्यं च॒ श्रेयस्तस्थैव तन्नप
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4369)
- **Original**: 13 कर्म चज्ञात्मकं श्रेय: फल स्वर्गाप्तिलक्षणम्‌ श्रेयः प्रधानं च फले तदेवानभिसंहिते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4370)
- **Original**: 14 । आत्मा ध्येगः सदा भूष योगयुक्तेस्तथा परम्‌। श्रेयस्तस्यैव संयोग: श्रेयो ब: परमात्मन:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4371)
- **Original**: 15 श्रेयांस्थेतवमनेकानि शातशोईथ सहस्तश:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4372)
- **Original**: सन्त्यत्न परमार्थस्तु न त्वेते श्रुयत्तां च मे ।। 16 धर्माय त्यज्यते किन्रु परमार्थों धन यदि । व्ययश्न क्रियते कस्मात्कामग्राप्त्युपलक्षण:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4373)
- **Original**: 97 पुत्रश्चेत्परमार्थ: स्थात्सोउप्यन्यस्थ नरेश्वर
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4374)
- **Original**: परमार्थभूत: सोउन्यस्य परमाथों हि तत्पिता
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4375)
- **Original**: 18 एवं न परमार्थोउस्ति जगत्यस्मिश्नराचरे । परमाथों हि कार्याण कारणानामशेषत:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4376)
- **Original**: 19 राज्यादिप्राप्तिसत्रोक्ता परमार्थनलया यदि। परमार्था भक्त्त्यत्न न भवत्ति च ये ततः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4377)
- **Original**: 20 ऋग्यजु:सामनिष्पाद्य॑ यज्ञकर्म मत॑ तब। परमार्थभूत॑ तत्रापि श्रूयतां गदतो मप
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4378)
- **Original**: 29 वि पुर है 8 है' उनके पास जानेको तत्पर हुआ हूँ
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4379)
- **Original**: किन्तु बीचहोगें, आपने जो वाक्य कहे हैं उन्हें सुनकर मेरा चित्त परमार्थ-अवण करनेके लिये आपकी ओर झुक गया है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4380)
- **Original**: है ट्विज ! ये कपिल्मुनि सर्वभूत भगवान्‌ विष्णुके ही अंछा हैं। इन्होंने संसारका मोह दूर करनेके ल्लिये ही पूृथिवीपर अबतार लिया है
- **Translation**: 

---

