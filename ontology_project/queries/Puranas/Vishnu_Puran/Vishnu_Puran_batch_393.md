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

### Verse 1 (Vishnu Puran 0.7841)
- **Original**: स तम्रैव च तस्थों
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.7842)
- **Original**: वासुदेवो5पि द्वारकामाजगाम
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.7843)
- **Original**: यावश्च बलभद्रोउवतस्थे._ तावद्धारत्त- राष्ट्री.. दुरयोधनस्तत्सकाशाद्दाशिक्षामशिक्षयत्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.7844)
- **Original**: वर्षत्रयान्ते च बश्नूप्रसेनप्रभृतिभि- यांदवैर्न तद्॒लले कृष्णेनापहरतमिति कृतावगति- विंदिहनगरी. गत्वा बलदेवस्सम्रत्याय्य ड्वारकामानीत:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.7845)
- **Original**: अक्रूरो5प्युत्तममणिसमुद्धृतसुवर्णेन भगवद्धब्वानपरोउनवरतं॑ यज्ञानियाज
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.7846)
- **Original**: सवनगतो हि क्षत्रियवैश्यो निम्नन्त्रह्महा भवतीत्ये- वम्प्रकारं दीक्षाकवर्च प्रविष्ट एवं तस्थो
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.7847)
- **Original**: द्विषष्टिवर्षाण्येब॑ तन्म्णिप्रभावात्त- ओषसर्गदुर्भिक्षमारिकामरणादिक नाभूत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.7848)
- **Original**: अथाक्रूरपक्षीयैभोजैइशञत्रुप्ते सात्वतस्थ प्रपोत्रे व्यापादिते भोजैस्सहाक्वूरो द्वारकामपहायापक्रान्त
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.7849)
- **Original**: तदसपक्रान्तिदिनादारभ्य तत्रोप बभूवु;
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.7850)
- **Original**: अथ यादवबलभद्रोग्रसेससमबेतो. मन्त्न- ममन्त्यदयूु भगवानुरगारिकेतन:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.7851)
- **Original**: किमिदमेकदैव प्रचुरोपद्रवागमनमेतदाल्ोच्यता- मिल्युक्तेजधकनामा यदुवृद्ध: प्राह
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.7852)
- **Original**: अस्पाक्रूरस्प पिता श्रफल्को सत्र यत्राभूत्तत्र तत्र दुर्भिक्षमारिकानावृष्टयादिक॑ नाभूत्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.7853)
- **Original**: काशिराजस्यथ विषये त्वनावृष्ठया च श्रफल्को चतुर्थ अंझ 277 क्रोघपृर्वक भगवान्‌ कासुदेबसे कहा--
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.7854)
- **Original**: “त॒मको घिक्रार है, तुम बड़े ही अर्थलेल्‌प हो; भाई होनेके कारण ही मैं तुम्हें क्षमा किये देता हूँ। तुम्हारा मार्ग खुला हुआ है, तुम खुशीसे जा सकते हो । अब मुझे तो द्वारकासे, तुमसे अथवा और सब सगे-सम्बन्धियोंसे कोई काम नहीं है। बस, मेरे आगे इन थोथी शपथोंका अब कोई प्रयोजन नहीं।' इस प्रकार उनको बातको काटकर बहुत कुछ मनानेपर भी वे वहाँ न रुके और विदेहनगस्कों चले गये
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.7855)
- **Original**: 101-102
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.7856)
- **Original**: विदेहनगरमें पहुँचनेपर राजा जनक उन्हें अर्घ्य देकर अपने धर ले आये और ने बहों रहने लगे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.7857)
- **Original**: 103-104
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.7858)
- **Original**: इधर, भगवान्‌ वासूदेज द्वारका्में चले आये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.7859)
- **Original**: जितने दिनॉतक बल्देवजो राजा जनकके यहाँ रहे उतने दिनतक धृतराष्ट्रका पुत्र दुर्योधन उनसे गदायुद्ध सीखता रहा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.7860)
- **Original**: अनन्तर, बभु और उम्रसेन आदि यादवॉफे, जिन्हें यह ठोक माऊूम था कि “कृष्णने स्थमन्तकमणि नहीं ली है', विदेहनगरमें जाकर जआपथपूर्वक विश्वास दिलानेपर बलदेवजी तीन वर्ष पश्चात्‌ ट्वास्कामें चले आये
- **Translation**: 

---

