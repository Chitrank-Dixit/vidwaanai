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

### Verse 1 (Vaivtpuran 18.18635)
- **Original**: » श्रीकृष्णस्तोत्राणि « <17 विप्रपत्नीकृतं श्रीकृष्णस्तोत्रम्‌ विप्रपल्य ऊचु: त्व॑ ब्रह्म परम॑ धाम निरीहों निरहंकृति:। निर्गुणश्ध॒ निराकार: साकारः सगुणः स्वयम्‌
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.18636)
- **Original**: साक्षिरूपश्च॒निर्लिप्त: परमात्मा निराकृति:। प्रकृति: पुरुषस्त्व॑ च कारणं च तथो: परम्‌
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.18637)
- **Original**: सृष्टिस्थित्यन्तविषये ये चर देवास्त्रय: स्पृता:। ते त्वदंशा: सर्वबीजा ब्रह्मविष्णुपहे श्वरा:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.18638)
- **Original**: यस्य लोप्लां च् बिबरे चाखिलं विश्वमीश्वर। महाविराड्‌ महाविष्णुस्त्व॑ तस्य जनको विभो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.18639)
- **Original**: तेजस्त्व॑ चापि तेजस्वी ज्ञानं ज्ञानी च तत्पर:
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.18640)
- **Original**: वेदेउनिर्वचनीयस्त्व॑ कस्त्वां स्तोतुमिहे भ्वर:
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.18641)
- **Original**: महदादि सृष्टिसूत्र पद्चतन्मात्रमेव. च । बीज त्वं॑ सर्वशक्तीनां सर्वशक्तिस्वरूपक:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.18642)
- **Original**: सर्वशक्तीश्वः सर्व: सर्वशकक्‍त्याश्रय: सदा। त्वमनीहः स्वयंज्योति: सर्वानन्द: सनातन:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.18643)
- **Original**: अहो5प्याकारहीनस्त्व॑ सर्वविग्रहवानपि
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.18644)
- **Original**: सर्वेन्द्रियाणां विषयं॑ जानासि नेन्द्रयी भवान्‌
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.18645)
- **Original**: सरस्वती जडीभूता यत्स्तोत्रे यत्रिरूपणे। जडीभूतो महेशभ्र शेषों धर्मों विधि: स्वयम्‌
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.18646)
- **Original**: पार्वती कमला राधा सावित्री बेदसूरपि। वेदश्ष जड़तां याति के वा शक्ता विपश्चित:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.18647)
- **Original**: वय॑ कि स्तवनं कुर्मः स्त्रियः प्राणेश्वरेश्वर। प्रस्नो भव नो देव दीनवन्धो कृपां कुरु
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.18648)
- **Original**: डति पेतुश्ष॒ ता विप्रपत्यस्तच्चरणाम्बुजे। अभयं प्रददौ ताभ्य: प्रसन्नवदनेक्षण:
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.18649)
- **Original**: विप्रपत्नीकृतं स्तोत्र पूजाकाले च्र यः पठेत्‌।स गति विप्रपत्नीनाँ लभते नात्र संशय:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.18650)
- **Original**: ्ञति श्रीब्रह्मवैवर्ते विप्रपत्नीकृत॑ श्रीकृष्णस्तोत्रं सम्पूर्णम्‌। ( श्रीकृष्णजन्मखण्ड 18। 36--48 ) 03/“-““ ये: थ40/:+2000 नागपत्नीकृतं श्रीकृष्णस्तोत्रम्‌ सुरसोवाच है जगत्कान्त कान्तं मे देहि मानं चर मानद । पतिः प्राणाध्चिकः स्त्रीणां नास्ति बन्धुक्ष तत्पर:
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.18651)
- **Original**: अयि सुरवरनाथ प्राणनाथं मदीय॑ न कुरु वश्वमनन्तप्रेमसिन्धों. सुबन्धो। अखिलभुवनबन्धो._ राधिकाप्रेमसिन्धो पतिमिह कुरू दान॑ मे विधातुर्विधात:
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.18652)
- **Original**: बत्रिनननविधिशेषा: षण्मुखश्रास्यसड्ैः स्तबनविषयजाड्या: स्तोतुमीशा न वाणी। न खलु निखिलवेदा: स्तोतुमन्येषपि देवा: स्तबनविषयशक्ता: सन्ति सन्‍्तस्तवैव
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.18653)
- **Original**: कुमतिरहमविज्ञा योधितां क्राधमा या क् भुवनगतिराशश्चक्षुषो5गोचरो5पि। विधिहरिहरशेषै:. स्तृयमानकश्ष॒ यस्त्वमतनुमनुजमीशं स्तोतुमिच्छामि त॑ त्वाम्‌
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.18654)
- **Original**: स्तवनविषयभीता पार्वती यस्य पद्मा श्रुतिगणजनयित्री स्तोतुमीशा न य॑ त्वाम्‌। कलिकलुषनिमग्रा._ वेदवेदाडुशास्त्श्रवणविषयमूढा. स्तोतुमिच्छाभि कि त्वाम्‌
- **Translation**: 

---

