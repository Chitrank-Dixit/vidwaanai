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

### Verse 1 (Markende Puran 0.2941)
- **Original**: त्ते दृष्टला तां समरादातुमुदामं चक्करुछता:। आकृष्टचापासिधरास्तथान्ये. तत्समीपगाः
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2942)
- **Original**: 2614 +संक्षित्त मार्कण्डेयपुराण « ऑजपकऋ हू 4 51 2392002#-/ हल्3 2 52524.6/642007 3 26644 003 22227 66444 77 >ज.2:2:52555#6#4 » डक ततः कोर चकारोच्चैरम्क्‍िका तानरीन्‌ प्रति। कोौपेन चास्‍्था भदन॑ परषोवर्णमभूत्तदा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2943)
- **Original**: 5 4 भ्रुकुटीकुटिलात्तस्या ललाटफलकादद्भतप्‌। काली करालवंदना विनिष्क्रान्तासिपाशिती
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2944)
- **Original**: 'बिचिव्र्खद्वाड्रश्ररा नरमालाविधूषणा। द्वीयिचर्मपरीआना. शुष्फरमांसातिभैरवा
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2945)
- **Original**: अतिविस्तारवदना. जिल्लाललनभीषणा। लिमग्रा रफक्तनयना भादापूरितदिकुपुखा
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2946)
- **Original**: सा वेगेनाभिपतिता घातयन्ती महासुरान्‌। सैन्ये क्त सुस़रीणामभक्षयत तदबलम्‌
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2947)
- **Original**: पार्णिग्राहाइकुशग्राहियोधछण्टासमन्वितानू । समादारयकहस्तेन मुखे चिक्षेप चारणान्‌
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2948)
- **Original**: तथैय योथ॑ तहुरंगे रथ सारधिना सह। निक्षिप्प वक्‍्बे दशैश्षर्वयन्त्यतिभेरथम्‌
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2949)
- **Original**: एक जग्राह केशेयु ग्रीवायामथ् ज्ापरम्‌। पादेनाक्रम्य चैवान्यमुरसान्यमपोथयत्‌
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2950)
- **Original**: नैमुक्तानि च शस्त्राणि महास्त्राणि तथासुर:। मुखेन जग्राह रुषा दशनमश्चितान्यपि
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2951)
- **Original**: बलिनां तद्‌ बल सर्वप्रसुरार्णा दुरात्मनाप्‌। म्दर्भिक्षवच्चान्यानन्यांशाताडयच्था
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2952)
- **Original**: अस्रिना निहता: के्चित्केचित्खट्वादुत्ाडिता:। जग्मुर्विनाशमसुरा. दन्ताग्राभिहतास्तथा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2953)
- **Original**: क्षणेन तद्‌ बल॑ सर्वभसुराणां निषातितम्‌। दृष्ताचण्डोउभिदुद्राव तां कालीमतिथीषणाम्‌
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2954)
- **Original**: शरवर्षमहाभीमैभीमाक्षी ता महासुर:। छादयाप्रास अक्रै श्र मुण्डः क्षितरि: सहस्नशः
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2955)
- **Original**: तानि चक्राण्यनेक्रानि विशमानानि तन्मुखम्‌। वर्भुर्वधार्कबिप्चानि सुग्रहनि घनौदरम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2956)
- **Original**: तलो जहासातिशषा भोम॑ भैरवनादिनी। उत्थाय च महासिं हइं देवी चण्डमधायत। गुहीत्वा आस्य केशेपु शिरस्तेनासिनाच्छिनत्‌
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2957)
- **Original**: ऋषि कहते हैं--
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2958)
- **Original**: तदनन्तर शुम्भकों आज्ञा पाकर थे चण्ड-मुण्ड आदि दैत्व चतुरक्िणों सेताके साथ अस्त्र-शस्त्रोंसे सुसज्जित ही चल दिये
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2959)
- **Original**: फिर गिरिराज हिमालयके: सुवर्णयय ऊँचे शिखरपर पहुँचकर उन्होंने सिंहपर बैठी हुई देवीको देखा। वे मन्द-मन्द पुसकरा रहा थीं
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2960)
- **Original**: उन्हें देखकर दैत्यलोग तत्परतासे पकड॒नेका उद्योग करते लगे। किसीने धनुष तान लिया. किसीने जलकार सँभालों और कृछ लोग देवीके पास आकर खड़े हो गये
- **Translation**: 

---

