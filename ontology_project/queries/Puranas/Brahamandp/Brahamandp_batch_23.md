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

### Verse 1 (Brahamandp 0.441)
- **Original**: 41 कथितो भीमसेनेन नगरातानयप्रिय:। विकलोपनीतविनता श्री राख्यो भागेवप्रिय:
- **Translation**: 

---

### Verse 2 (Brahamandp 0.442)
- **Original**: 42 सप्त गीसवना और महावृष्टिकता अष्टमा है और प्रह्मदान नवम है । इसके अनन्तर प्राजापत्य है
- **Translation**: 

---

### Verse 3 (Brahamandp 0.443)
- **Original**: नागयक्षाशक्षय विद्वान और तदुगोत्तर तथा है 36। पदक्रान्त-मृयक्रान्त-विषणुक्रान्त-मनोहरा । सूर्यकान्त धरेण्या-सन्‍्त कोकिलविश्र त है तेनवानित्यपवशपिशा चा-अतीवनही-साववित्र-अध॑ सावित्र और संतों भद्र है ।37-35। मनोहर-अधात्र्य और गन्धर्वानुपत है
- **Translation**: 

---

### Verse 4 (Brahamandp 0.444)
- **Original**: अलम्बु- बेष्ट-विष्णु और वेणवर ये दो हैं ।36। सागरा विजय और सर्वभुत मनोहर- हृतोत्सूष्ट-स्कन्ध और प्रिय जान लेना चाहिए ।40। जो मनोहर अधाश्नय तथा गन्घ॒वनिपत है
- **Translation**: 

---

### Verse 5 (Brahamandp 0.445)
- **Original**: अलम्बुषेष्ट की और नारद प्रिय है। 41
- **Translation**: 

---

### Verse 6 (Brahamandp 0.446)
- **Original**: नगरातान- प्रिय भी मसेन के द्वारा कहा गया है । विकलोपनीत विनता श्री नाम वाला भागंब को प्रिय है ।42। चतुर्दश तथा पंचदशेच्छंतीह नापद: । ससौवीरां सुसोवीरा ब्रह्मणो हयुपगीयते
- **Translation**: 

---

### Verse 7 (Brahamandp 0.447)
- **Original**: 43 उत्तरादिस्व रश्च॑व ब्रह्मा वे देवतास्त्रय: । हरिदेशसमुत्पन्ना हरिणस्थाव्यजायत
- **Translation**: 

---

### Verse 8 (Brahamandp 0.448)
- **Original**: 44 मूछ ना हरिणा ते वे चन्द्रस्यास्याधिदेवतम्‌ । करोपनीता विवृतावनुद्धि: स्व॒रमंडले
- **Translation**: 

---

### Verse 9 (Brahamandp 0.449)
- **Original**: 45 साकलोपनता तस्मान्मनुतस्यान्नदंबत: । मनुदेशाः समुत्पन्ना मूच्छ नाशुद्धमात्मना
- **Translation**: 

---

### Verse 10 (Brahamandp 0.450)
- **Original**: 46 तस्मात्तस्मास्मृगामार्गीमृ3गेंद्रोस्याधिदेवता । सावाश्रमसमाद्य मना अनेकापोरुषानखान्‌
- **Translation**: 

---

### Verse 11 (Brahamandp 0.451)
- **Original**: 46 मूच्छ नायोजना हयेषा स्याद्रजसारजनी ततः । तानि उत्तरतद्रांसपद्गदक्‍तक बिंदु:
- **Translation**: 

---

### Verse 12 (Brahamandp 0.452)
- **Original**: ।48 तस्मादुत्त रता यावत्प्रथमें स्वायमं बविदुः । तमोदुत्त रमंद्रोयदेवतास्या ध्रुबेत च
- **Translation**: 

---

### Verse 13 (Brahamandp 0.453)
- **Original**: गान्ध्र्व मूछना लक्षण
- **Translation**: 

---

### Verse 14 (Brahamandp 0.454)
- **Original**: [ 67 यहाँ पर चतुदंश और पठ्चदश की नारद इच्छा किया करते हैं ? ससोवीरा ओर सुसोौदीरा ब्रह्माजी की उपगीत की जाती हैं ।43
- **Translation**: 

---

### Verse 15 (Brahamandp 0.455)
- **Original**: और उत्तरादि स्वर है । ब्रह्मा तीन देवता हैं । हरि देश में समुत्पन्ना हरिण की हुई थी ।44। जो मूच्छ ना हरिणा है वे इस चन्द्रकी अधिदंवत हैं। निवृत्ति में करोपनोत स्व॒र॒मण्डल में अनुद्रि है ।45
- **Translation**: 

---

### Verse 16 (Brahamandp 0.456)
- **Original**: साकलोपनता है इसलिये मन उसका अन्नदेवत है
- **Translation**: 

---

### Verse 17 (Brahamandp 0.457)
- **Original**: मनुवेशा समुत्पन्ना मूज्छ ना आत्मा से शुद्ध है ।46। इससे मृगामार्गी मृगेन्द्र इसका अधिदेवता है। वह अनेक पोरुषा नखों को समुग्य मना है ।49। यह मूच्छ ना योजना रजसारजनीत से होतो है । उनको उत्तरमद्रांत सपद्‌ग दंबत जाननी चाहिए ।48। इस कारण से जब तक उत्त- रता हो तब तक इस्त स्वायम जानना चाहिए
- **Translation**: 

---

### Verse 18 (Brahamandp 0.458)
- **Original**: इस देयता तमोदुत्तर मन्द्रोम निश्चित रूप से समझना चाहिए
- **Translation**: 

---

### Verse 19 (Brahamandp 0.459)
- **Original**: 46। अपामदुत्तरत्वावधवतस्योत्तरायण: । स्थादिजमूछ नाहयेच पितर: श्रांद्धदेवत्ता:
- **Translation**: 

---

### Verse 20 (Brahamandp 0.460)
- **Original**: 450 शुद्धपड्जस्वयं कृत्वा यस्मादग्निमहर्षयः । उपति तस्मान्नजानीयाच्छ द्धयच्छिक रासभा:
- **Translation**: 

---

