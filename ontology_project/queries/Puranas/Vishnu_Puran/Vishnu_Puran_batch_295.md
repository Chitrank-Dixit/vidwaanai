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

### Verse 1 (Vishnu Puran 0.5881)
- **Original**: 39 पितृतीर्घेन सतिलं तथैव सलिलाझलिम्‌। प्रातामहेभ्यस्तेनेव पिष्डास्तीरथेंन निर्वपित्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5882)
- **Original**: 40 दक्षिणाग्रेषु पुष्पधूपादिपृजितम्‌ । स्वपित्रे प्रथम॑ पिण्ड द्दद्यादुच्छिष्टसन्निधों
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5883)
- **Original**: 49 पितामहाय चैवार्न्य तत्पित्रे च तथापरम्‌। दर्भभूले लेपभुज: प्रीणयेल्लेपघर्षणै:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5884)
- **Original**: 42 पिण्डैर्मातामहांस्तद्वद््धमाल्यादिसंयुतै: .
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5885)
- **Original**: पूजयित्वा द्विजाग्रयाणां द््याच्चाचमर्न तत:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5886)
- **Original**: 43 पितृभ्य: प्रथम भवत्या तन्मनस्को नरेश्वर । सुख्वधेत्याशिषा युक्तां दक्याच्छक्त्या च दक्षिणाम्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5887)
- **Original**: डंड॑ दत्वा च दक्षिणां तेभ्यो वाक्षयेद्रैश्वदेविकान्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5888)
- **Original**: प्रीयन्तामिह ये विश्वेदेवास्तेन इतीरयेत्‌
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5889)
- **Original**: '/ तथेति चोक्ते तैविंप्रै: प्रार्थीयास्तथाशिष: । पश्चाद्विसर्जयेद्रेवान्यूज॑.. पिन्न्यान्पहीपते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5890)
- **Original**: 46 मातामहानामसप्येव सह देवै: क्रम: स्मृतः । भोजने चर स्वशक्‍त्या च दाने तद्द्विसर्जने
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5891)
- **Original**: 47 आपादझौचनात्पूर्व कुयदिवह्िजन्मसु । बिसर्जन तु प्रथम पैत्रमातामहेषु वै
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5892)
- **Original**: 48 विसर्जयेत्रीतिवचस्सम्मान्याभ्यर्थितांस्तत: । निक्‍्तेंताभ्यनुज्ञात आद्वार॑ताननुव्रजेत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5893)
- **Original**: 49 भुज्ज्याश्षेैव सम॑ पूज्यभृत्यब्न्धुभिरात्मन:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5894)
- **Original**: 50 श्रीविष्णुपुराण ( अः 105 अत: उनकी सच्रिधिकि कारण समस्त राक्षस और असुरगण यहाँसे तुरन्त भाग जाये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5895)
- **Original**: तदनन्तर ब्राह्मणोंके तृप्त हो जानेपर थोड़ा-सा अन्न पृथिवीपर डाले और आचमनके लिये उन्हें एक-एक बार और जल दे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5896)
- **Original**: फिर भल्जी प्रकार तृष्त हुए उन आह्यणोंकी आज्ञा होनेपर समाहितचित्तसे पथिवीपर अन्न और तिलके पिण्ड-दान करें
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5897)
- **Original**: ओर पितृतीर्थसे तिलयुक्त जलाजलि दे तथा मातामह आदिको भी उस पितृतीर्थसे ही पिण्ड-दान करे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5898)
- **Original**: ब्राह्मणोंकी उच्छिष्ट (जूठन) के तिकट दक्षिणकी ओर अप्रभाग करके बिछाये हुए कुशाऑपर पहले अपने पिताके लिये पुष्प थूपादिसे पुजित पिण्डदान करे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5899)
- **Original**: तत्पश्चात्‌ एक पिण्ड पितामहके लिये और एक प्रपितामहके लिये दे और लेपभोजी पितृगणको तृप्त करे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5900)
- **Original**: इसी प्रकार गन्ध और माल्त्रदियुक्त पिण्डॉसे मातामह आदिका पूजन कर फिर ट्विजश्रेष्ठंको आयमन करावे
- **Translation**: 

---

