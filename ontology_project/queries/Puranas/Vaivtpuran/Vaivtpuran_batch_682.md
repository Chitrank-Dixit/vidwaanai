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

### Verse 1 (Vaivtpuran 92.19319)
- **Original**: निषेव्य मन्त्र देवानां जीवा जन्मनि जन्मनि । भेक्ता भवन्ति दुर्गाया: पादपडो सुदुर्लभे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 92.19320)
- **Original**: निषेव्य मन्त्र शम्भोश्व॒ जगतां कारणस्य च। तदा प्राप्रोति युववों: पादपद_ं सुदुर्लभम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 100.18949)
- **Original**: श्रीकृष्णस्तोत्राणि - <27 बह्यादिदेवगणै: कृतं श्रीकृष्णस्तोत्रम्‌ ब्रह्मोबाच नाथानिर्वचनीयो5सि भक्तानुग्रहविग्रह । बेदानिर्वचनीय॑ च कर्त्यां स्तोतुमिहे श्वर:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 100.18950)
- **Original**: श्रीमहादेव उबाच देहेषु देहिन॑ शश्वत्‌ स्थितं निर्लिप्तमेव च
- **Translation**: 

---

### Verse 5 (Vaivtpuran 100.18951)
- **Original**: कर्मिणां कर्मणां शुद्ध साक्षिणं साक्षतं विभुप्‌। किं स्तौमि रूपशून्य॑ च गुणशून्य॑ च निर्गुणम्‌
- **Translation**: 

---

### Verse 6 (Vaivtpuran 100.18952)
- **Original**: अनन्त उबाच कि वा जानाम्यहं नाथ त्वामज्ञोउनन्तमीश्वरम्‌ू। अनन्तकोटिब्लाह्माण्डकारणं दुःखतारणम्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 100.18953)
- **Original**: महाविष्णोश्व लोप्लां च विवरेषु जलेषु च
- **Translation**: 

---

### Verse 8 (Vaivtpuran 100.18954)
- **Original**: सन्ति विश्वान्यसंख्यानि चित्राणि कृत्रिमाणि च
- **Translation**: 

---

### Verse 9 (Vaivtpuran 100.18955)
- **Original**: सन्ति सन्तश्व देवाश्व ब्रह्मविष्णुशिवात्मका: । त्वदंशा: प्रतिबिप्बेषु तीर्थानि भारतं॑ तथा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 100.18956)
- **Original**: ब्रह्माण्डैकस्थितोडहहू च॒सूक्ष्मनागस्वरूपक: । स्थापितश्च॒॒त्वया कूर्मे गजेन्रे मशको यथा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 100.18957)
- **Original**: परमाणुपरं सूक्ष्म॑ विश्वेषु नास्ति कुत्नचित्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 100.18958)
- **Original**: महाविष्णों: परे स्थूल॑ समो नास्ति च कुत्रचित्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 100.18959)
- **Original**: महाविष्णो: परस्त्वं चर तत्परो नास्ति कश्नन । स्थूलात्‌ स्थूलतरों देव: सूक्ष्मात्‌ सूक्ष्मतमों महान्‌
- **Translation**: 

---

### Verse 14 (Vaivtpuran 100.18960)
- **Original**: आधारश्च महाविष्णोर्जलरूपो भवान्‌ स्वयम्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 100.18961)
- **Original**: जलाधारों हि गोलोकरस्त्व॑ च॒ स्थावररूपथृक्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 100.18962)
- **Original**: सर्वाधारों महान्‌ वायु: श्वासनिःश्रासरूपक: । भक्तानुग्रहदेहस्थ नित्यस्थ भवतो. विभो:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 100.18963)
- **Original**: वक्त्रै्बहुतरैवाॉथ त्ववा दत्ते: पुरैव च । स्तोतुमिच्छामि त्वद्योगं न दत्त ज्ञानमैश्वरम्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 100.18964)
- **Original**: देवा ऊचु: त्वामनन्तं यदि स्तोतुं देवोउनन्तो न हीक्वरः । न हि स्वयं विधाता च न हि ज्ञानात्मक: शिव:। सरस्वती जड़ीभूता किं कुर्मः स्तवर्न बयम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 100.18965)
- **Original**: मुनीन्द्रा ऊचुः बेदा न शक्ताः स्तोतुं चेत्त्वां चैव ज्ञातुमीक्षरम्‌ । बय॑ बेदबिद: सन्त: कि कुर्म: स्तबनं तब
- **Translation**: 

---

### Verse 20 (Vaivtpuran 100.18966)
- **Original**: डद स्तोत्र महापुण्य॑ देवैश्ष मुनिभि: कृतम्‌ । यः पठेत्संचत: शुद्ध: पूजाकाले चर भक्तितः
- **Translation**: 

---

