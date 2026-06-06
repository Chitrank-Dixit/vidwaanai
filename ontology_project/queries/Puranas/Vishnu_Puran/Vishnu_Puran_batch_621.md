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

### Verse 1 (Vishnu Puran 0.12401)
- **Original**: उत्पन्न होनेके समय उसका मुख मल, मूत्र, रक्त और वीर्य आदिमें लिपटा रहता है और उसके सम्पूर्ण अस्थिबन्धन प्रजापत्य (गर्भको सद्भुचित करनेवाली) बायुसे अत्यत्त पीड़ित होते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12402)
- **Original**: प्रबल प्रसूति-बायु उसका मुख नौचेको कर देती है और बह आतुर होकर बड़े क्लेशके साथ माताके गर्भाशयसे बाहर निकल पाता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12403)
- **Original**: है मुनिसत्तम ! उत्पन्न होनेके अनन्तर बाद्या बायुका रपर्श होनेसे अत्यत्त मूर्च्छित होकर वह जीव येसुध हो जाता है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12404)
- **Original**: उस समय वह जीव दुर्ग्थयुक्त फोड़ेमेंसे गिरे हुए किसी कण्टक-विद्ध अथवा आरेसे चौीरे हुए कीड़ेके समान पृथिवीपर गिरता है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12405)
- **Original**: उसे स्वय॑ खुजलाने अथवा करवट लेनेकी भी झक्ति नहीं रहती। वह स्लान
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12406)
- **Original**: 438 अशुचिप्रस्तरे सुप्त: कीटदंज्ञादिभिस्तथा । भरक्ष्यमाणो5पि नैवेषां समर्थों बिनिवारणे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12407)
- **Original**: 19 जन्मदुःखान्यनेकानि जन्मनो5नन्तराणि च । बारूभावे यदाप्रोति ह्ञाधिभौतादिकानि तु
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12408)
- **Original**: 20 अज्ञानतमसाउ5च्छन्नो मूढान्तः:करणो नरः । न जानाति कुतः कोउहं क्राहं गन्ता किमात्मन:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12409)
- **Original**: 21 केन बन्धेन बद्धो5ह॑ं कारएं किमकारणम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12410)
- **Original**: कि कार्य किमकार्य वा कि वाच्यं कि च नोच्यते
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12411)
- **Original**: 22 को धर्म: कश्न वाघर्म: कस्मिन्वरतेंय वा कथम्‌ । कि कर्तव्यमकर्तव्यं कि वा कि गुणदोषजत्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12412)
- **Original**: 23 एवं. पशुसमैर्मुढैरज्ञानप्रभव॑ महत्‌ । अवाप्यते नरैर्दःखं शिक्षोदरपरायणै:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12413)
- **Original**: 24 अज्ञान॑ तामसो भाव: कार्यारम्भप्रवृत्तय: । अज्ञानिनां प्रवर्तन्ते कर्मस्मेपास्ततो द्विज
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12414)
- **Original**: 25 नरक॑ कर्मणां ल्लोपात्फलमाहुर्मनीषिण: । तस्मादज्ञानिनां दुःखमिह चामुतन्र चोत्तमम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12415)
- **Original**: 26 जराजर्जरदेहश्ष॒ शिथिकावयव: पुप्तान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12416)
- **Original**: विगलच्छीर्णदेशनो वलिस्त्रायुशिरावृतः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12417)
- **Original**: 27 दूरप्रणष्टनयनो व्योमान्तर्गततारक: । नासाबिबरनिर्यातलोमपुझ्रश्लट् पु:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12418)
- **Original**: 28 ब्रकटीभूतसर्वास्थिर्नतपृष्ठास्थिसंहति:..। उत्सन्नजठराभित्वादल्पाहारो5ल्पचेष्टित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12419)
- **Original**: 29 कुच्छुचडक्रमणोत्थानशयनासनचेष्टित: । मनन्‍्दीभवच्छूत्रनेत्रस्सवल्लालावित्ानन:.
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12420)
- **Original**: 30 अनायत्तैस्समस्तैश करणैम॑रणोन्पुख: । तत्क्षणेउप्यनुभूतानामस्मर्ताखजिलवस्तुनाम्‌
- **Translation**: 

---

