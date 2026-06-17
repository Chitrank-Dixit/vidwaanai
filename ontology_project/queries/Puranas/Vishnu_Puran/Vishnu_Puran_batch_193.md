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

### Verse 1 (Vishnu Puran 0.3841)
- **Original**: 106 एबमेतत्पद॑ विष्णोस्तृतीयममलात्मकम्‌ । आधारधूतं लोकानां त्रयाणां वृष्टिकारणम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3842)
- **Original**: 107 ततः प्रभवति ब्रह्मन्सर्वपापहरा सरित्‌। गड्डा. देवाडुनाड्रानामनुलेपनपिक्लरा
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3843)
- **Original**: 108 यामपादाम्ब॒ुजाहुछननखस्नोतोबिनिर्गगाम्‌ू_। विष्णोर्बिभर्ति यां भकत्या झिरसाहतिश ध्रुव:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3844)
- **Original**: 109 ततः मप्तर्षयों यस्या: प्राणायामपरायणा: । तिष्ठन्ति वीचिमाल्म्रभिरुद्मामानजटा जले
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3845)
- **Original**: 110 वार्बोधैः सन्‍ततैर्यस्या: प्रावित शशिमण्डलम्‌ । भूयो5श्चिकतरां कान्ति वहत्येतदुह क्षये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3846)
- **Original**: 111 हे मैत्रेय ! जितने प्रदेझामें धुव स्थित है, पृथिवीसे लेकर उस प्रदेशपर्यन्त सम्पूर्ण देश प्रक्वकालमें नष्ट हो जाता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3847)
- **Original**: सप्नर्षियोंसे उत्तर-दिशामें ऊपरकी ओर जहाँ चूब स्थित है बह अति तेजोमय स्थान ही आकादा्यें विष्णुभगवानका तीसरा दिष्यधाम है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3848)
- **Original**: हे निप्र ! मुनिजनॉका यही परमस्थान है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3849)
- **Original**: पाप-पुण्यके नियृत्त हो जाने वधा देह-प्राप्तिके सम्पूर्ण कारणोंके नष्ट हो जानेपर प्राणिगण जिस स्थानपर जाकर फिर शोक नहीं करते वही भगवान्‌ विष्णुका परमपद है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3850)
- **Original**: जहाँ भगनानकी समान ऐश्र्यतासे प्राप्त हुए सोगद्वारा सतेज झोकर धर्म और घुव आदि लोक-साक्षिगण निवास करते हैं वहो भगबान्‌ विष्णुका परमपद है
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3851)
- **Original**: हे मैत्रेय ! जिसमें यह भूत, भविष्यत्‌ और वर्तमान चशाबर जगत्‌ ओतप्रोत हो रहा है बही भगवान्‌ विष्णुका परमपद है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3852)
- **Original**: जो तल्लीन योगिजनॉंकों आकाशमण्डल्फें डेदीप्यमान सूर्यके समान सबके प्रकादाकरूपसे प्रतीत होता है तथा जिसका विवेक-ज्ञानसे ही प्रत्यक्ष होता है वहीं भगवान्‌ विष्णुका परमपद है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3853)
- **Original**: है ट्विज ! उस विष्णुपदम्में हो सबके आधारभूत परम-तेजरवी धुव स्थित हैं, तथा धुबजीमें समस्त नक्षत्र, नक्षत्रों मेघ और मेघोंमें वृष्टि आश्रित है। हे महामुने ! उस वृष्टिसे ही समस्त सुष्टिका पोषण और सम्पूर्ण देव-सनुष्यादि प्राणियोंकी पुष्टि होती है
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3854)
- **Original**: 104-105
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3855)
- **Original**: तदनन्तर गौ आदि प्राणियोंसे उत्पन्न दुग्ध और घृत आदिकी आहतियोंसे परितुष्ट अश्रिदेव ही प्राणियोंकी स्थितिके लिये पुनः वृष्टिके कारण होते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3856)
- **Original**: इस प्रकार विष्णुभगवान्‌का यह निर्मल तृतीय लोक (धुब) ही व्रिजोकीका आधारभूत और वृष्टिका आदिकारण है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3857)
- **Original**: हे ऋह्मनू! इस विष्णुपदसे ही देवाड़्नाओंके अंगरागसे पाण्डुस्वर्ण हुई-सो सर्वपापापह्ारिणी श्रीगज्जाजी उत्पन्न हुई हैं
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3858)
- **Original**: विष्णुभगयानफ़े वाम 'चरण-कपलके अँगूठेके नखरूप स्रोतसे निकली हुई उन गक्नजजीकों धुव दिन-रातर अपने मस्तकपर धारण करता है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3859)
- **Original**: तदनन्तर जिनके जलमें खड़े होकर ज्ाणायाम-परायण सप्र्षिण उनकी. तरंगभंगीरो जटाऊल्मपके कम्पायमान होते हुए, अपमर्षण-मन्त्रका जप करते हैं तथा जिनके विस्तृत जलसमूहसे आछ्राक्ति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3860)
- **Original**: आ9] द्वितीय अंश 137 मेस्पृष्ठे पतत्युशैनिष्क्रात्ता झशिमण्डत्पत्‌। जगत: पावाार्थाव प्रयाति च॒ चतुर्दिशम्‌
- **Translation**: 

---

